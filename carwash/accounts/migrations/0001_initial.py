# Generated by Django 4.1.10 on 2024-04-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10, null=True, verbose_name='Rut')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Comuna')),
                ('Region', models.CharField(blank=True, max_length=150, null=True, verbose_name='Region')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-id'],
            },
        ),
    ]
