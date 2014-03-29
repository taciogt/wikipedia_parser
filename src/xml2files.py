## -*- coding: utf-8 -*-

import re

tag_open_title = '<title>'


def get_title(text):
    re.split()

file_path = 'files/ptwiki-latest-pages-articles-piece.xml'
extracted_files_folder = 'files/extracted/'

f = open(file_path)
text = f.read()
results = re.split('<page>', text)
print len(results)

for result in results:
    print result[0:100]

