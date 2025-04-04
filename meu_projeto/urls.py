"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # incluímos o include aqui também

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),  # conectamos as URLs do app forum
]
