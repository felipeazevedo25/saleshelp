from django.urls import path
from .views import login_user, register, logout_user, list_empresas, create_empresa, update_empresa, delete_empresa, export_excel

urlpatterns = [
    path('', login_user, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('list', list_empresas, name='list_empresas'),
    path('new', create_empresa, name='create_empresa'),
    path('update/<int:id>/', update_empresa, name='update_empresa'),
    path('delete/<int:id>/', delete_empresa, name='delete_empresa'),
    path('export_excel', export_excel, name='export_excel')
]
