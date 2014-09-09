import os

HOME_DIR = os.path.expanduser('~')
ROOT = os.path.join(HOME_DIR, 'wikipedia_files')

WIKI_DUMP = os.path.join(ROOT, 'ptwiki-latest-pages-articles.xml')

PAGES_DIR = os.path.join(ROOT, 'extracted_pages')
TEXTS_DIR = os.path.join(ROOT, 'extracted_texts')

wiki_full = '../files/ptwiki-latest-pages-articles.xml'
wiki_piece = '../files/ptwiki-latest-pages-articles-piece.xml'
pages_path = '../files/pages/'
all_pages_path = '../files/all_pages/'