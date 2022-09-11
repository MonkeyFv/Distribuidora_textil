#from django.shortcuts import render

from django.views import View
from app.models import *
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

#Tabla Empresa.
class empresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,NIT=""):
        if len(NIT)>0:
            emp=list(empresa.objects.filter(nit=NIT).values())
            if len(emp)>0:
                datos={"Mensaje":emp}
            else:
                datos={"Mensaje":"Tal empresa no existe."}
        else: 
            empr=list(empresa.objects.values())
            if len(empr)>0:
                datos={"Mensaje":empr}
            else:
                datos={"Mensaje":"No hay empresas."}
        return JsonResponse(datos)

    def post(self,request):
        datos2=json.loads(request.body)
        empres=empresa(empresa_id=datos2["ID"],nombre=datos2["Nombre"],direccion=datos2["Dirección"],telefono=datos2["Telef"],nit=datos2["NIT"])
        empres.save()
        respuesta={"Mensaje":"La empresa ha sido guardada"}
        return JsonResponse(respuesta)

    def put(self,request,NIT):
        datos3=json.loads(request.body)
        empresact=list(empresa.objects.filter(nit=NIT).values())
        if len(empresact)>0:
            emp=empresa.objects.get(nit=NIT)
            emp.nombre=datos3["Nombre"]
            emp.direccion=datos3["Dirección"]
            emp.telefono=datos3["Telefono"]
            emp.save()
            mensaje={"Mensaje":"Datos de la Empresa actualizado"}
        else:
            mensaje={"Mensaje":"No existe la empresa que buscas."}
        return JsonResponse(mensaje)

    def delete(self,request,NIT):
        empdelete=list(empresa.objects.filter(nit=NIT).values())
        if len(empdelete)>0:
            empresa.objects.get(nit=NIT).delete()
            mensaje={"Mensaje":"Datos de la empresa eliminados."}
        else:
            mensaje={"Mensaje":"La empresa a eliminar no existe."}
        return JsonResponse(mensaje)


