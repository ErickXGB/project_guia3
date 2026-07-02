from django import forms
from .models import Position, Employee

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'description', 'max_salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Desarrollador'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del cargo...'}),
            'max_salary': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ej. 1500.00'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'salary', 'hire_date', 'position', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pérez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'juan.perez@example.com'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


