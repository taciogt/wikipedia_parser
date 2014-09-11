## -*- coding: utf-8 -*-
__author__ = 'tacio'

import os
import sys

import file_paths


def print_inline(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def print_execution_time(start, end):
    processing_time = (end-start)
    hours = int(processing_time / 3600)
    minutes = int(processing_time / 60)
    seconds = int(processing_time % 60)
    print 'Processing time: ' + str(hours) + 'h ' + str(minutes) + 'min ' + str(seconds) + 's'


def read_file(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def save_file(path, content):
    text_file = open(path, 'w')
    text_file.write(content)
    text_file.close()


def set_django_env():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webmodule.webmodule.settings")


def remove_pages():
    number_of_pages = 0

    for root, dirs, files in os.walk(file_paths.PAGES_DIR):
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