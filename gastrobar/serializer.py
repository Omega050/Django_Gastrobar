from rest_framework import serializers
from gastrobar.models import Cliente, Reserva, Mesa, Prato, Bebida, ItemPedido, Pedido

class CLienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ['senha']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = '__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
