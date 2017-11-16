# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):

    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=titre)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre
