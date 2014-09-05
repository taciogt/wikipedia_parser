## -*- coding: utf-8 -*-
__author__ = 'tacio'

import os
import sys

import file_names


def print_inline(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def remove_pages():
    number_of_pages = 0

    for root, dirs, files in os.walk(file_names.all_pages_path):
        for f in files:
            file_path = os.path.join(root, f)
            if os.path.isfile(file_path):
                number_of_pages += 1
                if number_of_pages % 250 == 0:
                    print_inline('.')
                    if number_of_pages % 5000 == 0:
                        print_inline('\n' + str(number_of_pages) + ' páginas removidas. Removing: ' + str(file_path) + ' ')
                os.remove(file_path)
    print 'Total de páginas removidas: ' + str(number_of_pages)


if __name__ == '__main__':
    remove_pages()