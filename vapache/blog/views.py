# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')

# Part of Page

def header(request):

    return render(request, 'components/jumbotron.html')

def navbar(request):

    return render(request, 'components/navbar.html')
