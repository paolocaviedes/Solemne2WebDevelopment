# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from models import Categoria, Noticia
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def noticia_detalle(request):
    data = {}
    # categorias = {}

    data['object_list'] = Noticia.objects.all().order_by('-fechadePublicacion')
    print data
    template_name = 'noticia_detalle.html'
    return render(request, template_name, data)

def index(request):
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

# Create your views here.
