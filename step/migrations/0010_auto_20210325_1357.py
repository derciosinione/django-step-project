# Generated by Django 2.2.4 on 2021-03-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210325_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areas',
            name='subtitulo',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
