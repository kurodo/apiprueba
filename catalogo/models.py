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
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, blank = True, null=True)
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
        variaciones = Variacion.objects.filter(producto=self).order_by("order")
        llaves=Variacion.objects.filter(producto=self).values('llave').order_by('llave').distinct().count()
        nueva_variaciones = list(itertools.combinations(variaciones, llaves))

        for v in nueva_variaciones:
            keys=[]
            for item in v:
                keys.append(item.llave)
            myList = list(set(keys))
            if len(myList)==llaves:
                name = '%s' %(self.nombre)
                variaciones=[]
                for item in v:
                    name ='%s - %s' %(name,item.valor)
                    variaciones.append(item)
                existe = ProdcutoVariacion.objects.filter(nombre=name)
                if len(existe)==0:
                    pv=ProdcutoVariacion()
                    pv.producto=self
                    pv.nombre=name
                    pv.creador=user
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
    order = models.IntegerField(default=0)
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

class Categoria(models.Model):
    codigo = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100)
    subname = models.CharField(max_length=100, blank=True)
    padre = models.ForeignKey("Categoria",related_name="categoria_padre", null=True, on_delete=models.CASCADE)
    hijos = models.ManyToManyField("Categoria",related_name="categoria_hijos", blank=True)
    peso = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.padre:
            self.peso = self.padre.peso + 1
        super(Categoria, self).save(*args, **kwargs)
        if self.padre:
            self.padre.hijos.add(self)
            self.padre.save()
