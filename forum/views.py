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
    
    # Este return precisa estar dentro da função (e não fora dela)
    return render(request, 'forum/cadastro.html', {'form': form})

def home(request):
    return render(request, 'forum/home.html')
