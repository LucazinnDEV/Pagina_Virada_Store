from django.contrib import admin
from .models import Livro, Categoria, Perfil, Wishlist, Pedido, ItemPedido

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'preco', 'recomendado')  # Mostra o ID
    list_filter = ('recomendado', 'categoria')
    search_fields = ('titulo', 'autor')
    list_editable = ('recomendado',)
    readonly_fields = ('id',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    readonly_fields = ('id',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cpf')
    search_fields = ('nome', 'sobrenome', 'cpf')
    readonly_fields = ('id',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'livro')
    search_fields = ('user__username', 'livro__titulo')
    readonly_fields = ('id',)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ('livro', 'quantidade', 'subtotal')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('user__username',)
    inlines = [ItemPedidoInline]
    ordering = ('-criado_em',)
    readonly_fields = ('id',)

admin.site.register(Pedido, PedidoAdmin)
