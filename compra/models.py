from django.db import models
from catalogo.models import ProdcutoVariacion
from django.contrib.auth.models import User

TIPO_COMPRA=(
    ('bol', 'Boleta'),
    ('fac', 'Factura'),
    ('nn', 'Ninguna'),
)
# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=12, blank = True)
    direccion = models.CharField(max_length=200, blank = True)
    telefono = models.CharField(max_length=20, blank = True)
    correo = models.CharField(max_length=100, blank = True)
    comentario = models.TextField(max_length=100, blank = True)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateTimeField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    monto = models.IntegerField(default=0)
    tipo = models.CharField(max_length=3, choices=TIPO_COMPRA)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='compras', on_delete=models.CASCADE)
    producto = models.ForeignKey(ProdcutoVariacion, on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    unidad_compra = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    creador = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)

    def save(self, *args, **kwargs):
        self.total = (self.precio/100) * self.cantidad
        self.total = self.total*100
        super(DetalleCompra, self).save(*args, **kwargs)
        self.compra.monto = self.sumar_totales()
        self.compra.save()

    def sumar_totales(self):
        compras = DetalleCompra.objects.filter(compra = self.compra)
        total = 0
        for c in compras:
            total = total + c.total
        return total
