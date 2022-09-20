#from django.shortcuts import render
from django.views import View
from app.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

#Tabla Empresa.
class empresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, nit=""):
        if len(nit) > 0:
            emp = list(empresa.objects.filter(nit=nit).values())
            if len(emp) > 0:
                datos = {"Mensaje": emp}
            else:
                datos = {"Mensaje": "Tal empresa no existe."}
        else:
            empr = list(empresa.objects.values())
            if len(empr) > 0:
                datos = {"Mensaje": empr}
            else:
                datos={"Mensaje": "No hay empresas."}
        return JsonResponse(datos)

    def post(self, request):
        datos = json.loads(request.body)
        empres = empresa(empresa_id=datos["empresa_id"], nombre=datos["nombre"], direccion=datos["direccion"],
                         telefono=datos["telefono"], nit=datos["nit"])
        empres.save()
        respuesta = {"Mensaje": "La empresa ha sido guardada"}
        return JsonResponse(respuesta)

    def put(self, request, nit):
        datos = json.loads(request.body)
        empresact = list(empresa.objects.filter(nit=nit).values())
        if len(empresact) > 0:
            emp = empresa.objects.get(nit=nit)
            #emp.empresa_id = datos["empresa_id"]
            emp.nombre = datos["nombre"]
            emp.direccion = datos["direccion"]
            emp.telefono = datos["telefono"]
            emp.save()
            mensaje = {"Mensaje":"Datos de la Empresa actualizado"}
        else:
            mensaje = {"Mensaje":"No existe la empresa que buscas."}
        return JsonResponse(mensaje)

    def delete(self, request, nit):
        empdelete = list(empresa.objects.filter(nit=nit).values())
        if len(empdelete) > 0:
            empresa.objects.get(nit=nit).delete()
            mensaje={"Mensaje" : "Datos de la empresa eliminados."}
        else:
            mensaje={"Mensaje" : "La empresa a eliminar no existe."}
        return JsonResponse(mensaje)

class rolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, rolId=""):
        if len(rolId) > 0:
            rols = list(rol.objects.filter(rol_id=rolId).values())
            if len(rols) > 0:
                mensaje = {"mensaje": rols}
            else:
                mensaje = {"mensaje": "No se encontro rol"}
        else:
            rols = list(rol.objects.values())
            if len(rols) > 0:
                mensaje = {'rol': rols}
            else:
                mensaje = {"mensaje": "No se encontro rol"}
        return JsonResponse(mensaje)

    def post(self, request):
        datos = json.loads(request.body)
        rols = rol(rol_id=datos['rol_id'], tipo=datos['tipo'])
        rols.save()
        mensaje = {"mensaje": "Rol registrado exitosamente"}
        return JsonResponse(mensaje)

    def put(self,request,rolId):
        datos = json.loads(request.body)
        rols = list(rol.objects.filter(rol_id=rolId).values())
        if len(rols) > 0:
            ro = rol.objects.get(rol_id=rolId)
            ro.tipo = datos['tipo']
            ro.save()
            mensaje = {"mensaje": "Rol actualizado exitosamente"}
        else:
            mensaje = {"mensaje": "No se encontro Id"}
        return JsonResponse(mensaje)

    def delete(self, request, rolId):
        rols = list(rol.objects.filter(rol_id=rolId).values())
        if len(rols) > 0:
            rol.objects.filter(rol_id=rolId).delete()
            mensaje = {"mensaje": "Id eliminado exitosamente"}
        else:
            mensaje = {"mensaje": "No se encontro Id"}
        return JsonResponse(mensaje)

class usuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, userId=""):
        if len(userId) > 0:
            users = list(usuario.objects.filter(usuario_id=userId).values())
            if len(users) > 0:
                datos = {'mensaje': users}
            else:
                datos = {'mensaje': 'No se encontro usuario'}
        else:
            users = list(usuario.objects.values())
            if len(users) > 0:
                datos = {"mensaje": users}
            else:
                datos = {"mensaje": "no se encontraron usuarios. "}
        return JsonResponse(datos)

    def post(self, request):
        datos = json.loads(request.body)
        try:
            rol_id = rol.objects.get(rol_id=datos["rol_id"])
            user = usuario.objects.create(usuario_id=datos['usuario_id'], nombre=datos['nombre'], email=datos['email'], password=datos['password'],
                           telefono=datos['telefono'], rol_id=rol_id)
            user.save()
            mensaje = {"mensaje": "Usuario registrado exitosamente"}
        except rol.DoesNotExist:
            mensaje = {"mensaje":"Rol no existe"}
        return JsonResponse(mensaje)

    def delete(self,request, userId):
        user = list(usuario.objects.filter(usuario_id=userId).values())
        if len(user) > 0:
            usuario.objects.filter(usuario_id=userId).delete()
            mensaje = {"mensaje": "usuario eliminado exitosamente"}
        else:
            mensaje = {"mensaje": "No se encontro el usuario"}
        return JsonResponse(mensaje)

class empleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=""):
        if len(id) > 0:
            user = list(empleado.objects.filter(empleado_id=id).values())
            if len(user) > 0:
                datos = {"Mensaje": user}
            else:
                datos = {"Mensaje": "El empleado no existe."}
        else:
            usua = list(empleado.objects.values())
            if len(usua) > 0:
                datos = {"Mensaje":usua}
            else:
                datos = {"Mensaje": "No hay empresas."}
        return JsonResponse(datos)

    def post(self,request):
        datos=json.loads(request.body)
        try:
            idemp = empresa.objects.get(empresa_id=datos["empresa_id"])
            idreg = registro_contable.objects.get(contabilidad_id=datos["contabilidad_id"])
            iduser = usuario.objects.get(usuario_id=datos["usuario_id"])
            emplN = empleado.objects.create(empleado_id=datos["empleado_id"],empresa_id=idemp, registro_id=idreg, usuario_id=iduser)
            emplN.save()
            mensaje = {"Mensaje":"El empleado ha sido guardado"}
        except empresa.DoesNotExist:
            mensaje = {"Mensaje": "La empresa no existe"}
        except registro_contable.DoesNotExist:
            mensaje = {"Mensaje": "No se ha realizado registros"}
        except usuario.DoesNotExist:
            mensaje = {"Mensaje": "No existe el usuario"}
        return JsonResponse(mensaje)

    def put(self, request, id):
        datos = json.loads(request.body)
        useract = list(empleado.objects.filter(empleado_id=id).values())
        if len(useract) > 0:
            users = empleado.objects.get(emplado_id=id)
            idemp = empresa.objects.get(empresa_id=datos["empresa_id"])
            idreg = registro_contable.objects.get(contabilidad_id=datos["contabilidad_id"])
            iduser = usuario.objects.get(usuario_id=datos["usuario_id"])
            users.empresa_id = idemp
            users.regitro_id = idreg
            users.usuario_id = iduser
            users.save()
            mensaje = {"Mensaje":"Datos del Empleado actualizado"}
        else:
            mensaje = {"Mensaje":"No existe el empleado que buscas."}
        return JsonResponse(mensaje)

    def delete(self, request, id):
        userdelete = list(empleado.objects.filter(empleado_id=id).values())
        if len(userdelete) > 0:
            empleado.objects.get(empleado_id=id).delete()
            mensaje = {"Mensaje" : "Datos del empleado eliminados."}
        else:
            mensaje = {"Mensaje" : "El empleado a eliminar no existe."}
        return JsonResponse(mensaje)


class registroContableView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, cont=""):
        if len(cont) > 0:
            reg = list(registro_contable.objects.filter(contabilidad_id=cont).values())
            if len(reg) > 0:
                mensaje = {"Mensaje": reg}
            else:
                mensaje = {"Mensaje": "Este registro no existe"}
        else:
            regis = list(registro_contable.objects.values())
            if len(regis) > 0:
                mensaje = {"Mensaje": regis}
            else:
                mensaje = {"Mensaje": "No hay registros"}
        return JsonResponse(mensaje)

    def post(self, request):
        datos = json.loads(request.body)
        try:
            idemp = empresa.objects.get(empresa_id=datos["empresa_id"])
            regis = registro_contable.objects.create(contabilidad_id=datos['contabilidad_id'],empresa_id=idemp, cantidad=datos['cantidad'], valor=datos['valor'])
            regis.save()
            mensaje = {"Mensaje": "Registro creado!"}
        except empresa.DoesNotExist:
            mensaje = {"Mensaje": "La empresa no existe"}
        return JsonResponse(mensaje)

    def put(self, request, cont):
        datos = json.loads(request.body)
        regisact = list(registro_contable.objects.filter(contabilidad_id=cont).values())
        if len(regisact) > 0:
            idemp = empresa.objects.get(empresa_id=datos["empresa_id"])
            regis = registro_contable.objects.get(contabilidad_id=cont)
            regis.fecha = datos["fecha"]
            regis.empresa_id = idemp
            regis.valor = datos["valor"]
            regis.cantidad = datos["cantidad"]
            regis.save()
            mensaje = {"Mensaje": "Datos del registro actualizado"}
        else:
            mensaje = {"Mensaje": "No se puede actualizar porque el registro no existe"}
        return JsonResponse(mensaje)

    def delete(self, request, cont):
        registrodelete = list(registro_contable.objects.filter(contabilidad_id=cont).values())
        if len(registrodelete) > 0:
            registro_contable.objects.get(contabilidad_id=cont).delete()
            mensaje = {"Mensaje": "Registro eliminado"}
        else:
            mensaje = {"Mensaje": "No se pudo eliminar el registro"}
        return JsonResponse(mensaje)