from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', lambda request: redirect('home')),  
    path('home/', views.home, name='home'),  
    path('cadastro/', views.registrar_usuario, name='cadastro'),  
    path('categorias/', views.categorias, name='categorias'),  
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),  
    path('login/', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
