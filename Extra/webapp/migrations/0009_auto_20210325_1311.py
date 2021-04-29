# Generated by Django 2.2.4 on 2021-03-25 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_auto_20210325_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areas',
            name='criadoPor',
        ),
        migrations.AddField(
            model_name='areas',
            name='atualizadoPor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]