# Generated by Django 4.1.5 on 2023-01-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('repetir_senha', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('tipo_publico', models.CharField(max_length=20)),
                ('endereço', models.CharField(max_length=100)),
                ('numero_casa', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('tipo_usuario', models.IntegerField(default=0)),
            ],
        ),
    ]
