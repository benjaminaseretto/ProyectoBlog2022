from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio,name='inicio' ),
    path('post/', views.post,name='articulos'),
    path('postApi/', views.postapi),
    path('usuario/', views.usuario),
    path('busquedaPost/', views.buscarPost,name='buscador'),
    path('buscar/', views.buscar),
]