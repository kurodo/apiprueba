from django.contrib import admin
from .models import Producto, PrecioProducto, Variacion, ProdcutoVariacion
# Register your models here.


admin.site.register(Producto)
admin.site.register(PrecioProducto)
admin.site.register(Variacion)
admin.site.register(ProdcutoVariacion)
