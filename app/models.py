from django.db import models

class rol(models.Model):
    rol_id = models.CharField(max_length=50, primary_key=True)
    tipo = models.CharField(max_length=50, null=False)

class empresa(models.Model):
    empresa_id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=50, null=False)
    nit = models.CharField(unique=True, max_length=50)


class usuario(models.Model):
    usuario_id = models.CharField(max_length=50, primary_key= True)
    nombre = models.CharField(max_length= 50, null=False)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length= 50, null=False)
    telefono = models.CharField(max_length= 50, null=False)
    rol_id = models.ForeignKey(rol, on_delete=models.CASCADE,null=False)

class registro_contable(models.Model):
    contabilidad_id = models.CharField(primary_key=True, max_length=50)
    fecha = models.DateField(auto_now_add=True)
    empresa_id = models.ForeignKey(empresa, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)

class empleado(models.Model):
    empleado_id= models.CharField(primary_key=True, max_length=50)
    empresa_id= models.ForeignKey(empresa,on_delete=models.CASCADE)
    registro_id= models.ForeignKey(registro_contable, on_delete=models.CASCADE)
    usuario_id= models.ForeignKey(usuario, on_delete=models.CASCADE)

