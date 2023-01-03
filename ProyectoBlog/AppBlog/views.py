from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Post,Usuario,Categoria
from django.core import serializers
from AppBlog.forms import PostFormulario,UsuarioFormulario,CategoriaFormulario
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

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
    return HttpResponse(serializers.serialize('json',post_all))
    

def crear_post(request):
    post = Post(nombre ='PostTest', codigo_articulo = 199, numero_dia = 19)
    post.save()
    return HttpResponse(f'Post {post.articulo} ha sido creado')

def editar_post(request):
    articulo_consulta = 'PostTest'
    Post.objects.filter(articulo=articulo_consulta).update(articulo='NombrenuevoCursoTest')
    return HttpResponse(f'Post{articulo_consulta} ha sido actualizado')

 
def eliminar_post(request):
    articulo_nuevo='NombrenuevoCursoTest'
    post = Post.objets.get(articulo = articulo_nuevo)
    post.delete()
    return HttpResponse(f'Post{articulo_nuevo} ha sido eliminado')




class Postlist(ListView):
    model = Post
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/post_list.html'


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/AppBlog/post/list/'     

class PostEdite(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/AppBlog/post/list/'     

class PostDelete(DeleteView):
    model = Post
    template_name = 'AppBlog/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')
    success_url = '/AppBlog/post/list/'     


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/post_detail.html'


def usuarios(request):
    if request.method =="POST":

            usuFormulario = UsuarioFormulario(request.POST)
            print(usuFormulario)

            if usuFormulario.is_valid:
                informacion = usuFormulario.cleaned_data
                print(informacion)
                usuario = Usuario(usu_nom = informacion['usu_nom'], usu_ape = informacion['usu_ape'], usu_mail = informacion['usu_mail'])
                usuario.save()
                return render(request, "AppBlog/inicio.html")
    else:
        usuFormulario = UsuarioFormulario()
    return render (request,'AppBlog/usuarios.html')

def categorias(request):
    if request.method =="POST":

            caFormulario = CategoriaFormulario(request.POST)
            print(caFormulario)

            if caFormulario.is_valid:
                informacion = caFormulario.cleaned_data
                print(informacion)
                categorias = Categoria(cat_nombre = informacion['cat_nombre'], cat_id = informacion['cat_id'], cat_descripcion = informacion['cat_descripcion'])
                categorias.save()
                return render(request, "AppBlog/inicio.html")
    else:
        caFormulario = CategoriaFormulario()
    return render (request,'AppBlog/categorias.html')    

def usuariosapi(request):
    autores_todos= Usuario.objets.all()
    return HttpResponse(serializers.serialize('json',autores_todos))        

def categoriasapi(request):
    categorias_todos= Categoria.objets.all()
    return HttpResponse(serializers.serialize('json',categorias_todos))        

def buscarcategoria(request):
    return render(request,"AppBlog/busquedaCategorias.html")    

def buscarautor(request):
    return render(request,"AppBlog/busquedaAutores.html")        

def buscarCat(request):
    if request.GET['cat_id']:
            cat_nombre = request.GET['cat_id']
            categorias = Categoria.objects.filter(cat_id=cat_nombre)
            return render(request, "AppBlog/resultadoPost.html", {"categorias":categorias, "cat_id": cat_nombre})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)          


def buscarUsu(request):
    if request.GET['usu_ape']:
            usu_nom = request.GET['usu_ape']
            usuarios = Usuario.objects.filter(usu_ape=usu_nom)
            return render(request, "AppBlog/resultadoPost.html", {"autores":usuarios, "usu_ape": usu_nom})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)          



def leer_categorias(request):
    categorias_all = Categoria.objets.all()
    return HttpResponse(serializers.serialize('json',categorias_all))
    

def crear_categorias(request):
    categorias = Categoria(nombre ='CategoriaTest', cat_id = 199, cat_descripcion = 'tendencias globales')
    categorias.save()
    return HttpResponse(f'Categoria {categorias.cat_nombre} ha sido creado')

def editar_categorias(request):
    cat_nombre_consulta = 'CategoriaTest'
    Categoria.objects.filter(cat_nombre=cat_nombre_consulta).update(cat_nombre='NombrenuevoCategoriaTest')
    return HttpResponse(f'Categoria{cat_nombre_consulta} ha sido actualizado')

 
def eliminar_categorias(request):
    cat_nombre_nuevo='NombrenuevoCursoTest'
    categorias = Categoria.objets.get(cat_nombre = cat_nombre_nuevo)
    categorias.delete()
    return HttpResponse(f'Categoria{cat_nombre_nuevo} ha sido eliminado')




def leer_autores(request):
    autores_all = Usuario.objets.all()
    return HttpResponse(serializers.serialize('json',autores_all))
    

def crear_autores(request):
    autor = Usuario(nombre ='AutorTest', usu_ape = 'Aseretto', usu_mail = 'benjaaseretto@gmail.com')
    autor.save()
    return HttpResponse(f'Usuario {autor.usu_nom} ha sido creado')

def editar_autores(request):
    usu_nom_consulta = 'UsuarioTest'
    Usuario.objects.filter(usu_nom=usu_nom_consulta).update(usu_nom='NombrenuevoAutorTest')
    return HttpResponse(f'Usuario{usu_nom_consulta} ha sido actualizado')

 
def eliminar_autores(request):
    usu_nom_nuevo='NombrenuevoAutorTest'
    autor = Usuario.objets.get(usu_nom = usu_nom_nuevo)
    autor.delete()
    return HttpResponse(f'Usuario{usu_nom_nuevo} ha sido eliminado')


class Categorialist(ListView):
    model = Categoria
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/categorias_list.html'


class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    template_name='AppBlog/categorias_form.html'
    success_url = '/AppBlog/categorias/list/'     

class CategoriaEdite(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppBlog/categorias/list/'     

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'AppBlog/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')
    success_url = '/AppBlog/categorias/list/'     


class CategoriaDetail(DetailView):
    model = Categoria
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/categorias_list.html'


class Usuariolist(ListView):
    model = Usuario
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/usuario_list.html'


class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'
    success_url = '/AppBlog/usuario/list/'     

class UsuarioEdite(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = '/AppBlog/usuario/list/'     

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'AppBlog/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')
    success_url = '/AppBlog/usuario/list/'     


class UsuarioDetail(DetailView):
    model = Post
    queryset = Post.objects.order_by('articulo')
    template_name='AppBlog/usuarios_detail.html'

