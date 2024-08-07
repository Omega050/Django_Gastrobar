from django.contrib import admin
from gastrobar.models import Pedido, ItemPedido, Prato

class ItensPedido(admin.ModelAdmin):
    list_display = ('numero_pedido', 'item', 'quantidade')
admin.site.register(ItemPedido, ItensPedido)

class Pratos(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'disponivel')
admin.site.register(Prato, Pratos)

class Pedidos(admin.ModelAdmin):
    list_display = ('data', 'hora', 'preco')
admin.site.register(Pedido, Pedidos)