from django.urls import path
from .views import home, registrar_usuario

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', registrar_usuario, name='cadastro'),
]
