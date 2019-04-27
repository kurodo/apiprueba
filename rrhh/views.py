from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrabajadorSerializer, SalarioSerializer, PuestoSerializer, AsistenciaSerializer
from .models import Trabajador, Salario, Puesto, Asistencia

# Create your views here.
class TrabajadorViewSet(viewsets.ModelViewSet):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()

class SalarioViewSet(viewsets.ModelViewSet):
    serializer_class = SalarioSerializer
    queryset = Salario.objects.all()

class PuestoViewSet(viewsets.ModelViewSet):
    serializer_class = PuestoSerializer
    queryset = Puesto.objects.all()

class AsistenciaViewSet(viewsets.ModelViewSet):
    serializer_class = AsistenciaSerializer
    queryset = Asistencia.objects.all()
# Create your views here.
