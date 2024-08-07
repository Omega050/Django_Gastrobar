from datetime import datetime
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length= 100)
    email = models.EmailField(blank=False, max_length=30, null=False )
    cpf = models.CharField(max_length=11, unique=True)
    pswd = models.CharField(max_length=99, null=False)
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.AutoField(primary_key=True)
    data = models.DateField(default=datetime.now, blank=False)
    horario = models.TimeField(blank=False)

    def __str__(self):
        return str(self.numero)

class Pedido(models.Model):
    data = models.DateField(default= datetime.now, blank = False)
    hora = models.TimeField(blank=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.pk)

class ItemMenu(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2) 

    def __str__(self):
        return self.nome
    
    
class Prato(ItemMenu):
    descricao = models.TextField()
    disponivel = models.BooleanField(default=False, blank=False, null=False)

class Bebida(ItemMenu):
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    estoque = models.IntegerField

class ItemPedido(models.Model):
    item = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    numero_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, null=False)
