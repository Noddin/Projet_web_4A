# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article
from .forms import ContactForm, ArticleForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'derniers_articles': articles})

def article(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(articles)
    return render(request, 'addArticle.html', locals())

def editArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(articles)
    return render(request, 'editArticle.html', locals())

def deleteArticle(request,id):
   article = get_object_or_404(Article, id=id)
   article.delete()
   return redirect(articles)
