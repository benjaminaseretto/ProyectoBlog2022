from django import forms

class PostFormulario(forms.Form):
    articulo=forms.CharField()
    codigo_articulo=forms.IntegerField()
    numero_dia= forms.IntegerField()

class UsuarioFormulario(forms.Form):
    usu_nom=forms.CharField()
    usu_ape=forms.CharField()
    usu_mail=forms.CharField()

class CategoriaFormulario(forms.Form):
    cat_nombre=forms.CharField()
    cat_id=forms.IntegerField()
    cat_descripcion=forms.CharField()