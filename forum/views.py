from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from .forms import RegistroUsuarioForm
from .models import Perfil, Livro, Categoria
from django.db.models import Q


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            if Perfil.objects.filter(cpf=form.cleaned_data['cpf']).exists():
                messages.error(request, 'CPF já cadastrado.')
                return render(request, 'forum/cadastro.html', {'form': form})

            if Perfil.objects.filter(telefone=form.cleaned_data['telefone']).exists():
                messages.error(request, 'Telefone já cadastrado.')
                return render(request, 'forum/cadastro.html', {'form': form})

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Usuário já cadastrado.')
                return render(request, 'forum/cadastro.html', {'form': form})

            with transaction.atomic():  
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
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'forum/login.html', {'username': username})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'forum/login.html', {'username': username})

    return render(request, 'forum/login.html')

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Você saiu da conta.')
    return redirect('home')

def home(request):
    # Todos os livros
    livros = Livro.objects.all()
    # Top 10 mais vendidos
    mais_vendidos = Livro.objects.order_by('-vendas')[:10]
    # Top 10 recomendados (com base no campo booleano)
    recomendados = Livro.objects.filter(recomendado=True)[:10]
    context = {
        'livros': livros,
        'mais_vendidos': mais_vendidos,
        'recomendados': recomendados,
    }
    return render(request, 'forum/home.html', context)


def categorias(request):
    categorias = Categoria.objects.prefetch_related('livros').all()
    return render(request, 'forum/categorias.html', {'categorias': categorias})

def mais_vendidos(request):
    livros = Livro.objects.order_by('-vendas')[:10]
    return render(request, 'forum/mais_vendidos.html', {'livros': livros})

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

def ver_recomendados(request):
    livros = Livro.objects.filter(recomendado=True)
    return render(request, 'forum/recomendados.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'forum/detalhes_livro.html', {'livro': livro})

def buscar_livros(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Livro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(categoria__nome__icontains=query)
        )
        if not resultados.exists():
            mensagem = "Desculpe, não encontramos resultados para sua pesquisa. Tente novamente com outras palavras-chave."
            return render(request, 'forum/buscar.html', {'mensagem': mensagem, 'query': query})
    else:
        mensagem = "Por favor, insira um termo para buscar."
        return render(request, 'forum/buscar.html', {'mensagem': mensagem})

    return render(request, 'forum/buscar.html', {'resultados': resultados, 'query': query})