# Generated by Django 2.2.4 on 2021-03-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20210325_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='tel2',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
