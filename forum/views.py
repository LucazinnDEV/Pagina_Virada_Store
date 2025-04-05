from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Perfil

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(
                usuario=usuario,
                nome=form.cleaned_data['nome'],
                sobrenome=form.cleaned_data['sobrenome'],
                tipo_pessoa=form.cleaned_data['tipo_pessoa'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                cpf=form.cleaned_data['cpf'],
                cep=form.cleaned_data['cep'],
                endereco=form.cleaned_data['endereco'],
                telefone=form.cleaned_data['telefone'],
            )
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'forum/cadastro.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # Redirecionar para a página principal
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    messages.success(request, 'Você saiu da conta.')
    return redirect('home')

def home(request):
    return render(request, 'forum/home.html')

def categorias(request):
    return render(request, 'forum/categorias.html')

def mais_vendidos(request):
    return render(request, 'forum/mais_vendidos.html')