from django.urls import path
from app.views import *

urlpatterns=[
    path('Empresas/', empresaView.as_view(), name="Listado de Empresas"),
    path('Empresas/<str:nit>', empresaView.as_view(), name="Busqueda de Empresas"),
    path('Rol/', rolView.as_view(), name="Listado de roles"),
    path('Rol/<str:rolId>', rolView.as_view(), name="Busqueda de roles"),
    path('Usuario/', usuarioView.as_view(), name="Listado de usuarios"),
    path('Usuario/<str:userId>', usuarioView.as_view(), name="Busqueda de usuarios"),
    path('Empleado/', empleadoView.as_view(), name="Listado Empleados"),
    path('Empleado/<str:id>', empleadoView.as_view(), name="Buscar Empleados"),
    path('RegistroC/', registroContableView.as_view(), name="Listado Registros"),
    path('RegistroC/<str:cont>', registroContableView.as_view(), name="Búsqueda Registro")
]