from django.contrib import admin
from usuarios.models import TipoUsuario
from usuarios.models import Usuario


# Register your models here.

admin.site.register(TipoUsuario)
admin.site.register(Usuario)


