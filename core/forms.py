from django import forms
from .models import Empresa


class Empresa_form(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['status','cnpj','tipo', 'abertura', 'nome', 'fantasia', 'natureza_juridica', 'cep', 'municipio', 'uf', 'email', 'telefone', 'situacao', 'data_situacao']
