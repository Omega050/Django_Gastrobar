from django.contrib import admin
from gastrobar.models import Pedido, ItemPedido, Prato, Bebida, Cliente, Reserva, Mesa

class ItensPedido(admin.ModelAdmin):
    list_display = ('numero_pedido', 'item', 'quantidade')
    list_display_links=('item',)
    list_per_page = 20
admin.site.register(ItemPedido, ItensPedido)

class Pratos(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'disponivel')
    list_display_links=('nome',)
    list_per_page = 20
admin.site.register(Prato, Pratos)

class Bebidas(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'tamanho', 'estoque')
    list_display_links=('nome',)
    list_per_page = 20
admin.site.register(Bebida, Bebidas)

class Pedidos(admin.ModelAdmin):
    list_display = ('data', 'hora', 'preco')
    list_per_page = 20
admin.site.register(Pedido, Pedidos)

class Comandas(admin.ModelAdmin):
    list_display = ('')

class Clientes(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'email', 'celular')
    list_display_links=('cpf','nome')
    list_per_page = 20
admin.site.register(Cliente, Clientes)

class Reservas(admin.ModelAdmin):
    list_display = ('numero', 'mesa', 'cliente', 'data', 'horario')
    list_display_links = ('numero',)
    list_per_page = 20
admin.site.register(Reserva, Reservas)

class Mesas(admin.ModelAdmin):
    list_display = ('numero', 'status')
    list_display_links = ('numero',)
    list_per_page = 20
admin.site.register(Mesa, Mesas)