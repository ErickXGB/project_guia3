from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name="Descripción")
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Salario Máximo")

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def clean(self):
        super().clean()
        MIN_SALARY = 482.00
        if self.max_salary is not None:
            if self.max_salary < MIN_SALARY:
                raise ValidationError({
                    'max_salary': f'El salario máximo del cargo no puede ser menor al salario básico de Ecuador (${MIN_SALARY}).'
                })

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Correo")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sueldo")
    hire_date = models.DateField(verbose_name="Fecha de Ingreso")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Cargo")
    is_active = models.BooleanField(default=True, verbose_name="Estado Activo")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def clean(self):
        super().clean()
        
        # 1. Salary validations
        MIN_SALARY = 482.00
        MAX_SALARY = 20000.00
        
        if self.salary is not None:
            if self.salary < 0:
                raise ValidationError({'salary': 'El sueldo no puede ser negativo.'})
            if self.salary < MIN_SALARY:
                raise ValidationError({'salary': f'El sueldo no puede ser menor al salario básico de Ecuador (${MIN_SALARY}).'})
            if self.salary > MAX_SALARY:
                raise ValidationError({'salary': f'El sueldo es excesivamente alto (límite máximo permitido: ${MAX_SALARY}).'})
            
            # 2. Position limit validation
            if self.position and self.position.max_salary is not None:
                if self.salary > self.position.max_salary:
                    raise ValidationError({
                        'salary': f'El sueldo no puede superar el salario máximo permitido para el cargo de {self.position.name} (${self.position.max_salary}).'
                    })

        # 3. Hire date validation
        if self.hire_date is not None:
            if self.hire_date > datetime.date.today():
                raise ValidationError({'hire_date': 'La fecha de ingreso no puede ser una fecha futura.'})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



