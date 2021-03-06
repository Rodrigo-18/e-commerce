# Generated by Django 3.2.5 on 2021-07-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_produto_tipo_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='medida',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo_medida',
            field=models.CharField(choices=[('KG', 'kg'), ('G', 'g'), ('MG', 'mg'), ('L', 'L'), ('ML', 'ml')], max_length=2),
        ),
    ]
