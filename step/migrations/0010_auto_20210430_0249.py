# Generated by Django 2.2.4 on 2021-04-30 02:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0009_auto_20210430_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='dataModificacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categorias',
            name='dataRegisto',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
