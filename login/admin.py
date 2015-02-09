from django.contrib import admin
# Register your models here.

from usuarios.models import Usuario

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = Usuario


