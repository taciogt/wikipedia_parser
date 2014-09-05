#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
PROJECT_PATH = os.path.join(PROJECT_PATH, 'src')

ROOT_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    print ''

    sys.path.append(PROJECT_PATH)

    tests = unittest.TestLoader().discover(ROOT_PATH, "*tests.py")
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)