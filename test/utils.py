__author__ = 'tacio'


# coding:utf-8

__author__ = 'tacio'

import os
import re

FILES_DIR = 'files/created'


def find_link_tags():
    print __name__

    for root, dirs, files in os.walk(FILES_DIR, False):
        for f in files:
            f = os.path.join(root, f)
            f = open(f)
            text = f.read()

            pattern = r"\[\[.*?\]\]"
            matches = re.finditer(pattern, text)
            for match in matches:
                matched_str = match.group()
                if ':' in matched_str:
                    print matched_str


if __name__ == '__main__':
    print 'main'
    find_link_tags()