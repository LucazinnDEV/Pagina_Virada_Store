from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Perfil

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            perfil = Perfil.objects.create(
                usuario=user,
                nome=form.cleaned_data['nome'],
                sobrenome=form.cleaned_data['sobrenome'],
                tipo_pessoa=form.cleaned_data['tipo_pessoa'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                cpf=form.cleaned_data['cpf'],
                cep=form.cleaned_data['cep'],
                endereco=form.cleaned_data['endereco'],
                telefone=form.cleaned_data['telefone'],
            )

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'forum/cadastro.html', {'form': form})
# forum/views.py (complementa seu código atual)

def home(request):
    return render(request, 'forum/home.html')

def categorias(request):
    return render(request, 'forum/categorias.html')

def mais_vendidos(request):
    return render(request, 'forum/mais_vendidos.html')
