# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	slug=models.CharField(max_length=25)
	descripcion=models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	titulo = models.CharField(max_length=100)
	fechadePublicacion=models.DateTimeField(auto_now=False, auto_now_add=False)
	contenido=models.CharField(max_length=5000)
	imagen=models.ImageField(upload_to="newsImages")
	categoria=models.ForeignKey(Categoria)
	destacada=models.BooleanField()

	def __str__(self):
		return self.titulo

