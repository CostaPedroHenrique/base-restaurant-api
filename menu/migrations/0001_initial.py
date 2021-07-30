# Generated by Django 3.2.5 on 2021-07-30 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('icon', models.ImageField(upload_to='group_icons', verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('available', models.BooleanField(default=True, verbose_name='Disponível')),
                ('photo', models.ImageField(upload_to='group_icons', verbose_name='Ícone')),
                ('Grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.group')),
            ],
            options={
                'verbose_name': 'Prato',
                'verbose_name_plural': 'Pratos',
            },
        ),
    ]
