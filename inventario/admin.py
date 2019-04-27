from django.contrib import admin

from .models import Almacen, Movimiento, Inventario

admin.site.register(Almacen)
admin.site.register(Movimiento)
admin.site.register(Inventario)
