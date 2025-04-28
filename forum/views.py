from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from .models import Perfil, Livro, Categoria, Wishlist

# Registro de usuário
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

# Login de usuário
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

# Logout
def logout_usuario(request):
    logout(request)
    messages.success(request, 'Você saiu da conta.')
    return redirect('home')

# Página inicial
def home(request):
    livros = Livro.objects.all()
    mais_vendidos = Livro.objects.order_by('-vendas')[:10]
    recomendados = Livro.objects.filter(recomendado=True)[:10]
    desejos_count = Wishlist.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    context = {
        'livros': livros,
        'mais_vendidos': mais_vendidos,
        'recomendados': recomendados,
        'desejos_count': desejos_count,
    }
    return render(request, 'forum/home.html', context)

# Categorias
def categorias(request):
    categorias = Categoria.objects.prefetch_related('livros').all()
    return render(request, 'forum/categorias.html', {'categorias': categorias})

# Mais vendidos
def mais_vendidos(request):
    livros = Livro.objects.order_by('-vendas')[:10]
    return render(request, 'forum/mais_vendidos.html', {'livros': livros})

# Recomendados
def ver_recomendados(request):
    livros = Livro.objects.filter(recomendado=True)
    return render(request, 'forum/recomendados.html', {'livros': livros})

from .models import Wishlist

from django.shortcuts import render, get_object_or_404
from .models import Livro, Wishlist

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    is_in_wishlist = False
    if request.user.is_authenticated:
        is_in_wishlist = Wishlist.objects.filter(user=request.user, livro=livro).exists()

    return render(request, 'forum/detalhes_livro.html', {
        'livro': livro,
        'is_in_wishlist': is_in_wishlist,  # <-- passa essa variável para o template
    })

# Buscar livros
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
            mensagem = "Desculpe, não encontramos resultados para sua pesquisa."
            return render(request, 'forum/buscar.html', {'mensagem': mensagem, 'query': query})
    else:
        mensagem = "Por favor, insira um termo para buscar."
        return render(request, 'forum/buscar.html', {'mensagem': mensagem})

    return render(request, 'forum/buscar.html', {'resultados': resultados, 'query': query})

# Carrinho de compras
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

# Adicionar ao carrinho
from django.http import JsonResponse

def adicionar_ao_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(livro_id)] = carrinho.get(str(livro_id), 0) + 1
    request.session['carrinho'] = carrinho

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        total_itens = sum(carrinho.values())
        return JsonResponse({'mensagem': 'Livro adicionado com sucesso!', 'total_itens': total_itens})

    return redirect('carrinho')

# Remover do carrinho
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

# Remover todos de um item do carrinho
def remover_todos_do_carrinho(request, livro_id):
    carrinho = request.session.get('carrinho', {})

    if str(livro_id) in carrinho:
        del carrinho[str(livro_id)]
        request.session['carrinho'] = carrinho
        messages.success(request, "Livro removido completamente do carrinho.")

    return redirect('carrinho')

# Finalizar compra
def finalizar_compra(request):
    request.session['carrinho'] = {}
    messages.success(request, 'Compra finalizada com sucesso! Obrigado pela preferência.')
    return redirect('carrinho')

# Adicionar/remover livro da wishlist
@login_required
def toggle_wishlist(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, livro=livro)
    if not created:
        wishlist_item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# Ver wishlist
@login_required
def wishlist(request):
    desejos = Wishlist.objects.filter(user=request.user)
    return render(request, 'forum/wishlist.html', {'desejos': desejos})
