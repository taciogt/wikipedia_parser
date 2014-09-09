## -*- coding: utf-8 -*-

__author__ = 'tacio'

import os
import string

import markup_formatter
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
            # print root, f

            page_path = os.path.join(root, f)
            page_file = open(page_path, 'r')
            page_content = page_file.read()
            page_file.close()

            text = markup_formatter.format_text(page_content)

            text_dir = get_dir(f)
            text_path = os.path.join(text_dir, f)

            text_file = open(text_path, 'w')
            text_file.write(text)
            text_file.close()

            file_counter += 1
            if file_counter > 10:
                break
        if file_counter > 10:
            break


if __name__ == '__main__':
    iterate_over_files()