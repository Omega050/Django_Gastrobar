# Generated by Django 5.0.3 on 2024-08-08 11:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('pswd', models.CharField(max_length=99)),
                ('celular', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('hora', models.TimeField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('itemmenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gastrobar.itemmenu')),
                ('tamanho', models.CharField(max_length=10)),
                ('estoque', models.IntegerField(default=0)),
            ],
            bases=('gastrobar.itemmenu',),
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('itemmenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gastrobar.itemmenu')),
                ('descricao', models.TextField()),
                ('disponivel', models.BooleanField(default=False)),
            ],
            bases=('gastrobar.itemmenu',),
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastrobar.itemmenu')),
                ('numero_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastrobar.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('horario', models.TimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastrobar.cliente')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastrobar.mesa')),
            ],
        ),
    ]
