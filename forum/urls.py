from django.urls import path
from .views import registrar_usuario

urlpatterns = [
    path('cadastro/', registrar_usuario, name='cadastro'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.registrar_usuario, name='cadastro'),
    path('categorias/', views.categorias, name='categorias'),
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),
]
