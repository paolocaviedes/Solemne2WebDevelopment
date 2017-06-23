# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Categoria, Noticia
from django.urls import reverse

def noticia_detalle(request, id):
    noticia = get_object_or_404(Noticia, id = id)
    return render(request, 'noticia_detalle.html', {'noticia' : noticia,})

def index(request):
    destacatedNew = Noticia.objects.filter(destacada = True).order_by('-fechadePublicacion')[0]
    comunNew      = Noticia.objects.filter(destacada = False).order_by('-fechadePublicacion')[:6]
    return render(request, 'index.html', {'noticiaDestacada':destacatedNew,'noticiasComunes':comunNew,})

