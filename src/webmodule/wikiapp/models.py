from django.db import models


class Trigram(models.Model):

    first_word = models.CharField(max_length=50)
