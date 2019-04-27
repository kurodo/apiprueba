from django.db import models
from django.contrib.auth.models import User
import itertools
import collections
# Create your models here.
TIPO_PRODUCTO=(
    ('mc', 'Mercadería'),
    ('pt', 'Producto Terminado'),
    ('in', 'Insumo'),
    ('se', 'Servicio'),
    ('ee', 'Envases y embalajes '),
    ('sd', 'Suministros Diversos'),
    ('ot', 'Otros'),
)
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    codigo = models.CharField(max_length=100)
    descripcion = models.TextField(blank = True)
    fecha = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    imagen = models.ImageField(upload_to="producto", blank = True, null=True)
    tipo = models.CharField(max_length=3, choices=TIPO_PRODUCTO)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

    def crear_variaciones(self,user):
        variaciones = Variacion.objects.filter(producto=self)
        llaves=Variacion.objects.values('llave').order_by('llave').distinct().count()

        nueva_variaciones = list(itertools.combinations(variaciones, llaves))
        producto_variacion_now=ProdcutoVariacion.objects.filter(producto=self).values_list("variaciones")

        for v in nueva_variaciones:
            keys=[]
            for item in v:
                keys.append(item.llave)
            myList = list(set(keys))
            print(myList)

            if len(myList)==llaves:
                print("richard")
                print(v)
                print(producto_variacion_now)
                pv=ProdcutoVariacion()
                pv.producto=self
                pv.nombre='%s' %(self.nombre)
                pv.creador=user
                pv.save()
                for item in v:
                    pv.nombre='%s - %s' %(pv.nombre,item.valor)
                    pv.variaciones.add(item)
                    pv.save()


class PrecioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    fecha = models.DateTimeField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.producto

class Variacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,)
    llave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return "%s-%s" %(self.llave,self.valor)

class ProdcutoVariacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    variaciones = models.ManyToManyField(Variacion)
    imagen =  models.ImageField(upload_to="producto_variacion", blank = True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.nombre
