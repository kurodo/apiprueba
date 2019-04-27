from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer, VentaSerializer, DetalleVentaSerializer
from .models import Cliente, Venta, DetalleVenta

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()

class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSerializer
    queryset =  DetalleVenta.objects.all()
