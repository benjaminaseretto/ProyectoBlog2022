from django.db import models

# Create your models here.
class Post(models.Model):
    articulo=models.CharField(max_length=40)
    codigo_articulo=models.IntegerField()
    numero_dia= models.IntegerField()

class Usuario(models.Model):
    usu_nom=models.CharField(max_length=40)
    usu_ape=models.CharField(max_length=40)
    usu_mail=models.CharField(max_length=50)

class Categoria(models.Model):
    cat_nombre=models.CharField(max_length=40)
    cat_id=models.IntegerField()
    cat_descripcion=models.CharField(max_length=50)
 