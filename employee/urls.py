from django.urls import path
from . import views

app_name = 'employee'  # Defines the application namespace

urlpatterns = [
    path('', views.list_employees, name='list_employees'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]