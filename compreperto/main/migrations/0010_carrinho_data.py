# Generated by Django 3.2.5 on 2021-08-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_carrinho_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='data',
            field=models.DateField(auto_now=True, verbose_name='data_criação'),
        ),
    ]