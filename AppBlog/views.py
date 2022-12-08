from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Post
from django.core import serializers
from AppBlog.forms import PostFormulario

# Create your views here.
def buscar(request):
    if request.GET['codigo_articulo']:
            articulo = request.GET['codigo_articulo']
            post = Post.objects.filter(codigo_articulo=articulo)
            return render(request, "AppBlog/resultadoPost.html", {"posts":post, "codigo_articulo": articulo})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)          

def buscarPost(request):
    return render (request,'AppBlog/busquedaPost.html')

def inicio(request):
    return render (request,'AppBlog/inicio.html')

def post(request):
    if request.method =="POST":

            miFormulario = PostFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                print(informacion)
                post = Post(articulo = informacion['articulo'], codigo_articulo = informacion['codigo_articulo'], numero_dia = informacion['numero_dia'])
                post.save()
                return render(request, "AppBlog/inicio.html")
    else:
        miFormulario = PostFormulario()

    return render (request,'AppBlog/post.html',{"miFormulario" : miFormulario})

def usuario(request):
    return HttpResponse('Vista de usuarios')    

def postapi(request):
    post_todos= Post.objets.all()
    return HttpResponse(serializers.serialize('json',post_todos))        


def leer_post(request):
    post_all = Post.objets.all()
    return HttpResponse(post_all)
    

def crear_post(request):
    post = Post(nombre ='PostTest', codigo_articulo = 199, numero_dia = 19)
    post.save()

#def editar_post(request):


#def eliminar_post(request):