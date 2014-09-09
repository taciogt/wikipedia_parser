## -*- coding: utf-8 -*-

import os
import sys
import logging
import string

from file_paths import WIKI_DUMP, PAGES_DIR


# sample_test = False
# if sample_test:
#     wiki_path = file_names.wiki_piece
#     pages_path = file_names.pages_path
# else:
#     wiki_path = file_names.wiki_full
#     pages_path = file_names.all_pages_path


def extract_wiki_piece():
    wiki_full = open(file_names.wiki_full, 'r')
    wiki_piece = open(file_names.wiki_piece, 'w')
    wiki_piece.write(wiki_full.read(20000000))

    wiki_piece.close()
    wiki_full.close()


def remove_beggining_spaces(f):
    letter = f.read(1)
    while letter.isspace():
        letter = f.read(1)

    f.seek(-1, 1)

def extract_page_title(f):
    remove_beggining_spaces(f)
    
    letter = f.read(1)
    read_letters = ''

    title_begin = False
    title_end = False
    
    while letter != '' and not title_begin:
        read_letters += letter
        letter = f.read(1)
        title_begin = read_letters[-7:] == '<title>'

    if title_begin:
        read_letters = read_letters[7:]
    else:
        return '_no_title_begin_found'

    while letter != '' and not title_end:
        read_letters += letter
        letter = f.read(1)
        title_end = read_letters[-8:] == '</title>'

    if title_end:
        read_letters = read_letters[:-8]
        return read_letters

    return '_no_title_end_found'


def extract_page(f, pages_dir):
    title = extract_page_title(f)
    title = title.replace(os.sep, '-')

    remove_beggining_spaces(f)
    
    letter = f.read(1)
    read_letters = ''
    end_of_page = False
    
    while letter != '' and not end_of_page:
        read_letters += letter
        letter = f.read(1)
        end_of_page = read_letters[-7:] == '</page>'

    if end_of_page:
        read_letters = read_letters[0:-7]

    try:
        title_first_letter = title[0]
        title_first_letter = str.capitalize(title_first_letter)

        if title_first_letter in string.uppercase:
            page_dir = os.path.join(pages_dir, title_first_letter)
        else:
            page_dir = os.path.join(pages_dir, 'special-chars')

        if not os.path.isdir(page_dir):
                os.mkdir(page_dir)
        page_path = os.path.join(page_dir, str(title) + '.xml')

        page_file = open(page_path, 'w')
        page_file.write(read_letters)
        page_file.close()
    except Exception as e:
        logging.exception('deu merda!: ' + title)
        raise e

    return title


def extract_pages(origin_file, pages_dir):
    errors = []

    wiki_file = open(origin_file, 'r')

    page_counter = 0

    letter = wiki_file.read(1)
    read_letters = ''
    while letter != '':
        read_letters += letter
        if read_letters[-6:] == '<page>':
            try:
                title = extract_page(wiki_file, pages_dir)
                page_counter += 1
                read_letters = ''

                if page_counter % 200 == 0:
                    sys.stdout.write(".")
                    if page_counter % 10000 == 0:
                        sys.stdout.write('\n' + str(page_counter) + ' páginas')

                    sys.stdout.flush()
            except Exception as e:
                errors.append(e)

        letter = wiki_file.read(1)

    print errors

if __name__ == '__main__':

    extract_pages(WIKI_DUMP, PAGES_DIR)