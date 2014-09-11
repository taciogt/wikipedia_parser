## -*- coding: utf-8 -*-

__author__ = 'tacio'

import os

from file_paths import TEXTS_DIR
from utils import read_file, print_inline, set_django_env


def get_trigrams(text):
    trigrams = []

    sentences = text.split('.')

    for s in sentences:
        words = s.split()
        current_trigram = []
        for w in words:
            if len(current_trigram) == 3:
                current_trigram.pop(0)

            current_trigram.append(w)

            if len(current_trigram) == 3:
                trigrams.append(tuple(current_trigram))
    return trigrams


def iterate_over_files():
    file_counter = 0

    for root, dirs, files in os.walk(TEXTS_DIR):
        for f in files:

            if file_counter > 1:
                break

            text = read_file(os.path.join(root, f))

            print text[0:100]

            file_counter += 1

            if file_counter % 200 == 0:
                print_inline('.')
                if file_counter % 10000 == 0:
                    print_inline('\n' + str(file_counter) + ' páginas')


if __name__ == '__main__':
    set_django_env()
    iterate_over_files()
