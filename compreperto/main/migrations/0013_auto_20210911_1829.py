# Generated by Django 3.2.5 on 2021-09-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_carrinho_loja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='lojista',
            name='cpf',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(max_length=128, verbose_name='senha'),
        ),
        migrations.AlterField(
            model_name='lojista',
            name='senha',
            field=models.CharField(max_length=128, verbose_name='senha'),
        ),
    ]
