from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('home')),  # redireciona para /home
    path('home/', views.home, name='home'),  # precisa da view home
    path('cadastro/', views.registrar_usuario, name='cadastro'),  # já existe
    path('categorias/', views.categorias, name='categorias'),  # precisa da view
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),  # precisa da view
]
