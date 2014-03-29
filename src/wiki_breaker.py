## -*- coding: utf-8 -*-

import os
import logging

import file_names

sample_test = True
if sample_test:
    wiki_path = file_names.wiki_piece
    pages_path = file_names.pages_path
else:
    wiki_path = file_names.wiki_full
    pages_path = file_names.all_pages_path


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


def extract_page(f, page_counter):
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
        page_file = open(pages_path + str(title) + '.xml', 'w')
        page_file.write(read_letters)
        page_file.close()
    except Exception as e:
        logging.exception('deu merda!: ' + title)


def extract_pages():
    wiki_file = open(wiki_path, 'r')

    page_counter = 0

    letter = wiki_file.read(1)
    read_letters = ''
    while letter != '':
        read_letters += letter
        if read_letters[-6:] == '<page>':
            extract_page(wiki_file, page_counter)
            page_counter += 1
            read_letters = ''

        letter = wiki_file.read(1)


if __name__ == '__main__':

    extract_wiki_piece()

    extract_pages()