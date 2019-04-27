from django.db import models
from catalogo.models import ProdcutoVariacion
from django.contrib.auth.models import User
TIPO_ACCION=(
    ('au', 'Aumento'),
    ('di', 'Disminuyo'),
    ('tr', 'Transfirio'),
)
# Create your models here.
class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank = True)
    telefono = models.CharField(max_length=20, blank = True)
    ubigeo = models.CharField(max_length=100, blank = True)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    producto_variacion = models.ForeignKey(ProdcutoVariacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    accion = models.CharField(max_length=3, choices=TIPO_ACCION)
    cantidad = models.IntegerField(blank = True)
    unidad = models.CharField(max_length=100)
    al_origen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name="origen")
    al_destino =models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name="destino", blank=True)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)

class Inventario(models.Model):
    producto_variacion = models.ForeignKey(ProdcutoVariacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField(blank = True)
    unidad = models.CharField(max_length=200, blank = True)
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    almacen = models.CharField(max_length=100, blank = True)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)
