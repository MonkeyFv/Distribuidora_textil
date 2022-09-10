from django.db import models

class rol(models.Model):
    rol_id = models.AutoField(auto_created=True, primary_key=True)
    tipo = models.CharField(max_length=50, null=False)

class empresa(models.Model):
    empresa_id=models.AutoField(auto_created=True, primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    direccion=models.CharField(max_length=50, null=False)
    telefono=models.CharField(max_length=50, null=False)
    nit=models.CharField(unique=True, max_length=50)

class estado_financiero(models.Model):
    estado_financiero_id=models.AutoField(auto_created=True, primary_key=True) #verbosename o choices.
    estado=models.IntegerField(null=False)
    cantidad=models.IntegerField(null=False)

class usuario(models.Model):
    usuario_id = models.AutoField(auto_created=True, primary_key= True)
    nombre = models.CharField(max_length= 50, null=False)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length= 50, null=False)
    telefono = models.CharField(max_length= 50, null=False)
    rol_id = models.ForeignKey(rol, on_delete=models.CASCADE)

class registro_contable(models.Model):
    contabilidad=models.CharField(primary_key=True, max_length=50)
    fecha=models.DateField(auto_now=True)
    empresa_id= models.ForeignKey(empresa, on_delete=models.CASCADE)
    estado_financiero_id=models.ForeignKey(estado_financiero, on_delete=models.CASCADE)
    valor=models.IntegerField(null=False)

class empleado(models.Model):
    empleado_id= models.AutoField(auto_created=True, primary_key=True)
    empresa_id= models.ForeignKey(empresa,on_delete=models.CASCADE)
    registro_id= models.ForeignKey(registro_contable, on_delete=models.CASCADE)
    usuario_id= models.ForeignKey(usuario, on_delete=models.CASCADE)

class userempleado(models.Model): #Relación 1:1
    registro=models.AutoField(auto_created=True,primary_key=True)
    fecha=models.DateField(auto_now=True)