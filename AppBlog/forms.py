from django import forms

class PostFormulario(forms.Form):
    articulo=forms.CharField()
    codigo_articulo=forms.IntegerField()
    numero_dia= forms.IntegerField()
