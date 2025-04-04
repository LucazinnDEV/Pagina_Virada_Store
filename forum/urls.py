from django.urls import path
from .views import registrar_usuario

urlpatterns = [
    path('cadastro/', registrar_usuario, name='cadastro'),
]
