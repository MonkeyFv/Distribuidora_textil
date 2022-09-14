from django.urls import path
from app.views import *

urlpatterns=[
    path('Empresas/',empresaView.as_view(),name="Listado de Empresas"),
    path('Empresas/<str:NIT>',empresaView.as_view(),name="Busqueda de Empresas"),
    path('Empleado',empleadoView.as_view(),name="Listado Empleados"),
    path('Empleado/<int:ID>',empleadoView.as_view(),name="Buscar Empleados")
]