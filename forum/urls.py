from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('home/', views.home, name='home'),
    path('cadastro/', views.registrar_usuario, name='cadastro'),
    path('categorias/', views.categorias, name='categorias'),
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),
]
