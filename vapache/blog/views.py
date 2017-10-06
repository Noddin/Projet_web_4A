# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'derniers_articles': articles})

def lire(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article': article})
