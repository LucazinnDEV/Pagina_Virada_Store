from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'forum/cadastro.html', {'form': form})

from django.shortcuts import render
def home(request):
    return render(request, 'forum/home.html')

def categorias(request):
    return render(request, 'forum/categorias.html')

def mais_vendidos(request):
    return render(request, 'forum/mais_vendidos.html')