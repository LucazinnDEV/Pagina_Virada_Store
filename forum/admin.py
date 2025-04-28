from django.contrib import admin
from .models import Livro, Categoria, Perfil, Wishlist

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'preco', 'recomendado')  # Adiciona coluna "Recomendado" no admin
    list_filter = ('recomendado', 'categoria')  # Filtro lateral por recomendado e categoria
    search_fields = ('titulo', 'autor')  # Caixa de busca no admin
    list_editable = ('recomendado',)  # Permite editar "recomendado" direto da lista

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'sobrenome', 'cpf')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'livro')
    search_fields = ('user__username', 'livro__titulo')
