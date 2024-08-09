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

class Mesa(models.Model):
    numero = models.AutoField(primary_key=True)
    status = models.BooleanField()

class Reserva(models.Model):
    numero = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesa, on_delete = models.CASCADE, blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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

class Comanda(models.Model):
    numero = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, null = True, on_delete=models.SET_NULL)
    valorTotal = models.DecimalField(max_digits=6, decimal_places=2) 
    data = models.DateField(default= datetime.now, blank = False)
    hora_abertura = models.TimeField(blank=False)
    hora_fechamento = models.TimeField(blank=False)

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
    estoque = models.IntegerField(blank=False, default=0)

class ItemPedido(models.Model):
    item = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)
    numero_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.quantidade} x {self.item.nome}"