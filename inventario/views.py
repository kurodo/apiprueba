from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlmacenSerializer, MovimientoSerializer, InventarioSerializer
from .models import Almacen, Movimiento, Inventario

# Create your views here.
class AlmacenViewSet(viewsets.ModelViewSet):
    serializer_class = AlmacenSerializer
    queryset = Almacen.objects.all()

class MovimientoViewSet(viewsets.ModelViewSet):
    serializer_class = MovimientoSerializer
    queryset = Movimiento.objects.all()

class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
