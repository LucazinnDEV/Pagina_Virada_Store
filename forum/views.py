from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Perfil, Livro, Categoria


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
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'forum/login.html')

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Você saiu da conta.')
    return redirect('home')

def home(request):
    livros = Livro.objects.all()
    return render(request, 'forum/home.html', {'livros': livros})

def categorias(request):
    categorias = Categoria.objects.prefetch_related('livros').all()
    return render(request, 'forum/categorias.html', {'categorias': categorias})

def mais_vendidos(request):
    return render(request, 'forum/mais_vendidos.html')

def adicionar_ao_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(livro_id)] = carrinho.get(str(livro_id), 0) + 1
    request.session['carrinho'] = carrinho
    messages.success(request, 'Livro adicionado ao carrinho!')
    return redirect('home')

def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    livros = []
    total = 0

    for livro_id, quantidade in carrinho.items():
        try:
            livro = Livro.objects.get(id=livro_id)
            subtotal = livro.preco * quantidade
            total += subtotal
            livros.append({
                'livro': livro,
                'quantidade': quantidade,
                'subtotal': subtotal,
            })
        except Livro.DoesNotExist:
            continue

    return render(request, 'forum/carrinho.html', {
        'livros': livros,
        'total': total,
    })

def adicionar_ao_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(livro_id)] = carrinho.get(str(livro_id), 0) + 1
    request.session['carrinho'] = carrinho
    messages.success(request, 'Livro adicionado ao carrinho.')
    return redirect('carrinho')

def remover_do_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})

    livro_id_str = str(livro_id)
    if livro_id_str in carrinho:
        if carrinho[livro_id_str] > 1:
            carrinho[livro_id_str] -= 1
        else:
            del carrinho[livro_id_str]

        request.session['carrinho'] = carrinho
        messages.success(request, 'Livro removido do carrinho.')

    return redirect('carrinho')

def remover_todos_do_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})

    if str(livro_id) in carrinho:
        del carrinho[str(livro_id)]
        request.session['carrinho'] = carrinho
        messages.success(request, "Livro removido completamente do carrinho.")

    return redirect('carrinho')

def finalizar_compra(request):
    request.session['carrinho'] = {}
    messages.success(request, 'Compra finalizada com sucesso! Obrigado pela preferência.')
    return redirect('carrinho')