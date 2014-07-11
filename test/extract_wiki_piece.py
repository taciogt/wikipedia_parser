# coding:utf-8

__author__ = 'tacio'

import os


TEST_FILES_DIR = 'files/created'
WIKI_FILE = 'ptwiki-latest-pages-articles.xml'
WIKI_FILE_PATH = os.path.join(os.path.pardir, 'files', WIKI_FILE)
WIKI_PIECE_FILE = 'ptwiki-piece.xml'
WIKI_PIECE_FILE_PATH = os.path.join(TEST_FILES_DIR, WIKI_PIECE_FILE)


def delete_previous_file():
    if os.path.exists(WIKI_PIECE_FILE_PATH):
        os.remove(WIKI_PIECE_FILE_PATH)


def file_walker(original_file_path, new_file_path, pages_number=4):
    pages_counter = 0

    with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
        read_word = ''
        page_start = False
        page_end = False

        while True:
            read_letter = original_file.read(1)
            new_file.write(read_letter)

            read_word += read_letter

            if read_word == '<page>':
                page_start = True
            elif read_word == '</page>':
                page_end = True
            elif read_word not in '<page>' and read_word not in '</page>':
                read_word = ''


            if page_start and page_end:
                pages_counter += 1
                page_start = False
                page_end = False

            if pages_counter >= pages_number:
                break


def run():
    delete_previous_file()
    file_walker(WIKI_FILE_PATH, WIKI_PIECE_FILE_PATH, 50)


if __name__ == '__main__':
    run()