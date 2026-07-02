from django.contrib import admin
from .models import Position, Employee

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'max_salary')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'salary', 'hire_date', 'position')
    list_filter = ('position', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')

