from django.contrib import admin

from .models import Empresa

admin.site.register(Empresa)

class Empresa_admin(admin.ModelAdmin):
    list_display = ['fantasia', 'cnpj', 'natureza_juridica', 'cep', 'email', 'telefone', 'situacao', 'data_situacao',]