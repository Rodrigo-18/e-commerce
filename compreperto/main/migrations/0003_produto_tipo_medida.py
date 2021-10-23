# Generated by Django 3.2.5 on 2021-07-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210728_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo_medida',
            field=models.CharField(choices=[('KG', 'kg'), ('G', 'g'), ('MG', 'mg'), ('L', 'L'), ('ML', 'ml')], default='KG', max_length=2),
        ),
    ]