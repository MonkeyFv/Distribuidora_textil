from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(rol)
admin.site.register(empresa)
admin.site.register(usuario)
admin.site.register(registro_contable)
admin.site.register(empleado)