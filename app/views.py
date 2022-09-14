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

class empleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,ID=0):
        if ID>0:
            user=list(empleado.objects.filter(empleado_id=ID).values())
            if len(user)>0:
                datos={"Mensaje":user}
            else:
                datos={"Mensaje":"Tal empresa no existe."}
        else: 
            usua=list(empresa.objects.values())
            if len(usua)>0:
                datos={"Mensaje":usua}
            else:
                datos={"Mensaje":"No hay empresas."}
        return JsonResponse(datos)

    def post(self,request):
        datos1=json.loads(request.body)
        try:
            idemp=empresa.objects.get(empresa_id=datos1["ID Empresa"])
            idreg=registro_contable.objects.get(contabilidad=datos1["Registro"])
            iduser=usuario.objects.get(usuario_id=datos1["ID User"])
            emplN=empleado.objects.create(empresa_id=idemp,registro_id=idreg,usuario_id=iduser)
            emplN.sabe()
            mensaje={"Mensaje":"El empleado ha sido guardado"}
        except empresa.DoesNotExist:
            mensaje={"Mensaje":"La empresa no existe"}
        except registro_contable.DoesNotExist:
            mensaje={"Mensaje":"No se ha realizado registros"}
        except usuario.DoesNotExist:
            mensaje={"Mensaje":"No existe el usuario"}
        return JsonResponse(mensaje)

    def put(self,request,ID):
        datos3=json.loads(request.body)
        useract=list(empresa.objects.filter(nit=ID).values())
        if len(useract)>0:
            users=empleado.objects.get(nit=ID)
            users.empresa_id=datos3["ID Empresa"]
            users.regitro_id=datos3["ID Registro"]
            users.save()
            mensaje={"Mensaje":"Datos del Empleado actualizado"}
        else:
            mensaje={"Mensaje":"No existe el empleado que buscas."}
        return JsonResponse(mensaje)

    def delete(self,request,ID):
        userdelete=list(empresa.objects.filter(empleado_id=ID).values())
        if len(userdelete)>0:
            empleado.objects.get(empleado_id=ID).delete()
            mensaje={"Mensaje":"Datos del empleado eliminados."}
        else:
            mensaje={"Mensaje":"El empleado a eliminar no existe."}
        return JsonResponse(mensaje)