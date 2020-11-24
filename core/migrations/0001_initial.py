# Generated by Django 3.1.3 on 2020-11-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=100, verbose_name='status')),
                ('message', models.CharField(default='', max_length=100, verbose_name='message')),
                ('cnpj', models.CharField(default='', max_length=100, verbose_name='cnpj')),
                ('tipo', models.CharField(default='', max_length=100, verbose_name='tipo')),
                ('abertura', models.CharField(default='', max_length=100, verbose_name='abertura')),
                ('nome', models.CharField(default='', max_length=100, verbose_name='nome')),
                ('fantasia', models.CharField(default='', max_length=100, verbose_name='fantasia')),
                ('natureza_juridica', models.CharField(default='', max_length=100, verbose_name='natureza_juridica')),
                ('logradouro', models.CharField(default='', max_length=100, verbose_name='logradouro')),
                ('numero', models.CharField(default='', max_length=100, verbose_name='numero')),
                ('complemento', models.CharField(default='', max_length=100, verbose_name='complemento')),
                ('cep', models.CharField(default='', max_length=100, verbose_name='cep')),
                ('bairro', models.CharField(default='', max_length=100, verbose_name='bairro')),
                ('municipio', models.CharField(default='', max_length=100, verbose_name='municipio')),
                ('uf', models.CharField(default='', max_length=100, verbose_name='uf')),
                ('email', models.CharField(default='', max_length=100, verbose_name='email')),
                ('telefone', models.CharField(default='', max_length=100, verbose_name='telefone')),
                ('situacao', models.CharField(default='', max_length=100, verbose_name='situacao')),
                ('data_situacao', models.CharField(default='', max_length=100, verbose_name='data_situacao')),
                ('motivo_situacao', models.CharField(default='', max_length=100, verbose_name='motivo_situacao')),
                ('capital_social', models.CharField(default='', max_length=100, verbose_name='capitalsocial')),
                ('socioNome', models.CharField(default='', max_length=100, verbose_name='qsa.nome')),
            ],
        ),
    ]