from django.shortcuts import render

# forum/views.py
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')  # ou qualquer outra página
    else:
        form = RegistroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})
