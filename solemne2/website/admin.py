# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria,Noticia

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','slug','descripcion')

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('id','titulo','fechadePublicacion','contenido','imagen','categoria','destacada')


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Noticia,NoticiaAdmin)