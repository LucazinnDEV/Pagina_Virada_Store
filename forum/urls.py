from django.urls import path
from .views import home, registrar_usuario

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', registrar_usuario, name='cadastro'),
]
<<<<<<< HEAD

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.registrar_usuario, name='cadastro'),
    path('categorias/', views.categorias, name='categorias'),
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),
]
=======
>>>>>>> aa1d869fba86a8894fd54008d56838d273f3eb02
