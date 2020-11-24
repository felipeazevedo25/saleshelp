from django.shortcuts import render, redirect
from .models import Empresa
from .forms import Empresa_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import datetime
import xlwt


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list_empresas')
        else:
            messages.info(request, 'Usuário ou Senha incorreta')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='/login/')
def list_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})


@login_required(login_url='/login/')
def create_empresa(request):
    form = Empresa_form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_empresas')

    return render(request, 'empresa_form.html', {'form': form})


@login_required(login_url='/login/')
def update_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    form = Empresa_form(request.POST or None, instance=empresa)

    if form.is_valid():
        form.save()
        return redirect('list_empresas')

    return render(request, 'empresa_form.html', {'form': form, 'empresa': empresa})


@login_required(login_url='/login/')
def delete_empresa(request, id):
    empresa = Empresa.objects.get(id=id)

    if request.method == 'POST':
        empresa.delete()
        return redirect('list_empresas')

    return render(request, 'prod-delete-confirm.html', {'empresa': empresa})


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Dispositions'] = 'attachment; filename=Empresas' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Empresas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['status','cnpj','tipo', 'abertura', 'nome', 'fantasia', 'natureza_juridica', 'cep', 'municipio', 'uf', 'email', 'telefone', 'situacao', 'data_situacao']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Empresa.objects.all().values_list('status','cnpj','tipo', 'abertura', 'nome', 'fantasia', 'natureza_juridica', 'cep', 'municipio', 'uf', 'email', 'telefone', 'situacao', 'data_situacao')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response