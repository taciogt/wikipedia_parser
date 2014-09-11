# -*- coding: utf8 -*-

__author__ = 'tacio'


from django.test import TestCase


from utils import set_django_env

set_django_env()


class TestTrigramsSaving(TestCase):

    def test_check_files(self):
        self.fail()
