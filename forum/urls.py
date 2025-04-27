from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Livros e categorias
    path('categorias/', views.categorias, name='categorias'),
    path('mais-vendidos/', views.mais_vendidos, name='mais_vendidos'),
    path('recomendados/', views.ver_recomendados, name='recomendados'),
    path('<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),

    # Usuário
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),

    # Carrinho
    path('adicionar-ao-carrinho/<int:livro_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover-do-carrinho/<int:livro_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('remover-todos-do-carrinho/<int:livro_id>/', views.remover_todos_do_carrinho, name='remover_todos_do_carrinho'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),

    # Pesquisa
    path('buscar/', views.buscar_livros, name='buscar_livros'),
]
