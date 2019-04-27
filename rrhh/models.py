from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

TIPO_SALARIO=(
    ('hor', 'Hora'),
    ('sem', 'Semanal'),
    ('qui', 'Quincenal'),
    ('men', 'Mensual'),
    ('pro', 'Produccion'),
)
# Create your models here.
class Trabajador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    nombre = models.CharField(max_length=100, blank = True)
    dni = models.CharField(max_length=8, blank = True)
    direccion = models.CharField(max_length=200, blank = True)
    telefono = models.CharField(max_length=20, blank = True)
    correo = models.CharField(max_length=100, blank = True)
    def __str__(self):
        return self.nombre

@receiver(post_save, sender=User)
def create_usuario_trabajador(sender, instance, created, **kwargs):
    if created:
        Trabajador.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.trabajador.save()

class Salario(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    salario = models.IntegerField()
    modalidad = models.CharField(max_length=5, choices=TIPO_SALARIO)

class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    superior = models.ManyToManyField('self', blank=True)
    subordinado = models.ManyToManyField('self', blank=True)

class Asistencia(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
