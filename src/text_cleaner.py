## -*- coding: utf-8 -*-

__author__ = 'tacio'

import os
import string
import time

import markup_formatter
from utils import read_file, save_file, print_inline, print_execution_time
from file_paths import PAGES_DIR, TEXTS_DIR


def get_dir(file_name):
    first_letter = str.capitalize(file_name[0])
    if first_letter in string.ascii_uppercase:
        dir_name = first_letter
    else:
        dir_name = 'special-char'

    dir_path = os.path.join(TEXTS_DIR, dir_name)

    if not os.path.isdir(dir_path):
                os.mkdir(dir_path)

    return dir_path


def iterate_over_files():
    file_counter = 0

    for root, dirs, files in os.walk(PAGES_DIR):
        for f in files:

            page_path = os.path.join(root, f)
            page_content = read_file(page_path)

            text = markup_formatter.format_text(page_content)

            text_dir = get_dir(f)
            text_path = os.path.join(text_dir, f)

            save_file(text_path, text)

            file_counter += 1

            if file_counter % 200 == 0:
                print_inline('.')
                if file_counter % 10000 == 0:
                    print_inline('\n' + str(file_counter) + ' páginas')


if __name__ == '__main__':
    start = time.time()

    iterate_over_files()

    end = time.time()
    print_execution_time(start, end)