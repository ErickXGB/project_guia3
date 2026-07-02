from django.urls import path
from . import views

urlpatterns = [
    # Positions (Cargos)
    path('cargos/', views.position_list, name='position_list'),
    path('cargos/nuevo/', views.position_create, name='position_create'),
    path('cargos/<int:pk>/', views.position_detail, name='position_detail'),
    path('cargos/editar/<int:pk>/', views.position_edit, name='position_edit'),
    path('cargos/eliminar/<int:pk>/', views.position_delete, name='position_delete'),
    path('cargos/reporte/pdf/', views.position_report_pdf, name='position_report_pdf'),
    path('cargos/reporte/excel/', views.position_report_excel, name='position_report_excel'),

    # Employees (Empleados)
    path('', views.home_view, name='home'),
    path('empleados/', views.employee_list, name='employee_list'),
    path('empleados/nuevo/', views.employee_create, name='employee_create'),
    path('empleados/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('empleados/editar/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('empleados/eliminar/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('empleados/reporte/pdf/', views.employee_report_pdf, name='employee_report_pdf'),
    path('empleados/reporte/excel/', views.employee_report_excel, name='employee_report_excel'),
    path('cambiar-vista/', views.toggle_view_mode, name='toggle_view_mode'),
]
