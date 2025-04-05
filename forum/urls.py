from django.urls import path
from .views import home, registrar_usuario

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', registrar_usuario, name='cadastro'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # acessa a home quando for /
    path('cadastro/', views.registrar_usuario, name='cadastro'),  # acessa /cadastro/
]











