from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_hired', 'position', 'salary']
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'First name'
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Phone'
            }),
            'date_hired': forms.DateInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Date d\'hired',
                'type': 'date'
            }),
            'position': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Position'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Salary'
            })
        }
