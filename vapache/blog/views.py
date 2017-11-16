# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.

    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():

        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer

        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.

    return render(request, 'contact.html', locals())

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'addArticle.html', locals())

def editArticle(request, id):
    #article = get_object_or_404(Article, id=id)
    #form = ArticleForm(request.POST or None, instance=article)
    #if form.is_valid():
    #    form.save()
    return render(request, 'editArticle.html', locals())
