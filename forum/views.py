from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from decimal import Decimal
from django.utils import timezone
from .models import Perfil
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil, Livro, Categoria, Wishlist, Pedido, EventoPedido, ItemPedido

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
                usuario = form.save()  # Cria o User

                # Agora cria manualmente o perfil completo
                Perfil.objects.create(
                    user=usuario,
                    cpf=form.cleaned_data['cpf'],
                    telefone=form.cleaned_data['telefone'],
                    data_nascimento=form.cleaned_data['data_nascimento'],
                    foto=None  # ou algo como request.FILES.get('foto'), se quiser
                )

            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'forum/cadastro.html', {'form': form})

# Login

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
    return render(request, 'forum/home.html', {
        'livros': livros,
        'mais_vendidos': mais_vendidos,
        'recomendados': recomendados,
        'desejos_count': desejos_count,
    })

# Categorias
def categorias(request):
    categorias = Categoria.objects.prefetch_related('livros').all()
    return render(request, 'forum/categorias.html', {'categorias': categorias})

# Recomendados
def ver_recomendados(request):
    livros = Livro.objects.filter(recomendado=True)
    return render(request, 'forum/recomendados.html', {'livros': livros})

# Detalhes do livro
def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    is_in_wishlist = False
    if request.user.is_authenticated:
        is_in_wishlist = Wishlist.objects.filter(user=request.user, livro=livro).exists()
    return render(request, 'forum/detalhes_livro.html', {
        'livro': livro,
        'is_in_wishlist': is_in_wishlist,
    })

# Busca
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
            return render(request, 'forum/buscar.html', {
                'mensagem': "Desculpe, não encontramos resultados para sua pesquisa.",
                'query': query
            })
    else:
        return render(request, 'forum/buscar.html', {
            'mensagem': "Por favor, insira um termo para buscar."
        })
    return render(request, 'forum/buscar.html', {'resultados': resultados, 'query': query})

# Carrinho
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
    request.session.modified = True
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        total_itens = sum(carrinho.values())
        return JsonResponse({'mensagem': 'Livro adicionado com sucesso!', 'total_itens': total_itens})
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
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        messages.error(request, 'Seu carrinho está vazio.')
        return redirect('carrinho')
    request.session['carrinho'] = {}
    messages.success(request, 'Compra finalizada com sucesso! Obrigado pela preferência.')
    return redirect('carrinho')

@login_required
def toggle_wishlist(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, livro=livro)
    if not created:
        wishlist_item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def wishlist(request):
    desejos = Wishlist.objects.filter(user=request.user)
    return render(request, 'forum/wishlist.html', {'desejos': desejos})

def confirmar_finalizacao(request):
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect('carrinho')

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

    return render(request, 'forum/confirmar_finalizacao.html', {
        'livros': livros,
        'total': total,
    })

def _get_cart_items(request):
    cart = request.session.get('carrinho', {})
    itens, total = [], Decimal('0.00')
    for pk, qtd in cart.items():
        try:
            livro = Livro.objects.get(pk=pk)
            subtotal = livro.preco * qtd
            itens.append({
                'livro': livro,
                'quantidade': qtd,
                'subtotal': subtotal,
            })
            total += subtotal
        except Livro.DoesNotExist:
            continue
    return itens, total

@login_required
def checkout(request):
    itens, total = _get_cart_items(request)
    if request.method == 'POST':
        pedido = Pedido.objects.create(
            user=request.user,
            total=total,
            criado_em=timezone.now()
        )
        agora = timezone.now()

        # Salvar os itens do pedido
        for item in itens:
            ItemPedido.objects.create(
                pedido=pedido,
                livro=item['livro'],
                quantidade=item['quantidade'],
                subtotal=item['subtotal']
            )

        # Criar evento inicial
        EventoPedido.objects.create(
            pedido=pedido,
            status='Pedido Recebido',
            data=agora.date(),
            hora=agora.time(),
            local='Processando pagamento',
            detalhes='Aguardando confirmação do pedido.'
        )

        request.session['carrinho'] = {}
        request.session.modified = True
        return redirect('obrigado')
    return render(request, 'forum/checkout.html', {
        'livros': itens,
        'total': total,
    })

def obrigado(request):
    return render(request, 'forum/obrigado.html')

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).order_by('-criado_em')
    return render(request, 'forum/meus_pedidos.html', {
        'pedidos': pedidos
    })
def mais_vendidos(request):
    livros = Livro.objects.order_by('-vendas')[:10]
    return render(request, 'forum/mais_vendidos.html', {'livros': livros})
@login_required
def rastrear_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    eventos = pedido.eventos.order_by('-data', '-hora')
    return render(request, 'forum/rastreamento_pedido.html', {
        'pedido': pedido,
        'eventos': eventos
    })

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'forum/editar_perfil.html', {'form': form})

@login_required
def perfil_usuario(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    return render(request, 'forum/perfil.html', {'perfil': perfil})