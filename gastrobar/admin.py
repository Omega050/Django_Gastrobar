from django.contrib import admin
from gastrobar.models import Pedido, ItemPedido, Prato, Bebida, Cliente

class ItensPedido(admin.ModelAdmin):
    list_display = ('numero_pedido', 'item', 'quantidade')
    list_display_links=('item')
admin.site.register(ItemPedido, ItensPedido)

class Pratos(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'disponivel')
    list_display_links=('nome')
admin.site.register(Prato, Pratos)

class Bebidas(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'disponivel')
    list_display_links=('nome')
admin.site.register(Bebida, Bebidas)

class Pedidos(admin.ModelAdmin):
    list_display = ('item', 'data', 'hora', 'preco')
admin.site.register(Pedido, Pedidos)

class Comandas(admin.ModelAdmin):
    list_display = ('')

class Clientes(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'email', 'celular')
    list_display_links=('cpf','nome')
admin.site.register(Cliente, Clientes)