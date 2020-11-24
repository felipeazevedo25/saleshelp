from django.db import models

class Empresa(models.Model):
    status = models.CharField('status', max_length=100, default='')
    cnpj = models.CharField('cnpj', max_length=100, default='')
    tipo = models.CharField('tipo', max_length=100, default='')
    abertura = models.CharField('abertura', max_length=100, default='')
    nome = models.CharField('nome', max_length=100, default='')
    fantasia = models.CharField('fantasia', max_length=100, default='')
    natureza_juridica = models.CharField('natureza_juridica', max_length=100, default='')
    cep = models.CharField('cep', max_length=100, default='')
    municipio = models.CharField('municipio', max_length=100, default='')
    uf = models.CharField('uf', max_length=100, default='')
    email = models.CharField('email', max_length=100, default='')
    telefone = models.CharField('telefone', max_length=100, default='')
    situacao = models.CharField('situacao', max_length=100, default='')
    data_situacao = models.CharField('data_situacao', max_length=100, default='')

    def __str__(self):
        return str(self.fantasia)