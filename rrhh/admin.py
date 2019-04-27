from django.contrib import admin

# Register your models here.
from .models import Trabajador, Salario, Puesto, Asistencia

class TrabajadorAdmin(admin.ModelAdmin):
    fields = ('nombre','dni','usuario')

admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Salario)
admin.site.register(Puesto)
admin.site.register(Asistencia)
