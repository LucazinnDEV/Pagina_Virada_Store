from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')  # ajuste conforme sua URL de login
    else:
        form = RegistroUsuarioForm()
    return render(request, 'forum/cadastro.html', {'form': form})


from django.shortcuts import render
def home(request):
    return render(request, 'forum/home.html')
