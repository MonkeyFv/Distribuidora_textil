from django.urls import path
from app.views import *

urlpatterns=[
    path('Empresas/',empresaView.as_view(),name="Listado de Empresas"),
    path('Empresas/<str:NIT>',empresaView.as_view(),name="Busqueda de Empresas")
]