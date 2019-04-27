from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProveedorSerializer, CompraSerializer, DetalleCompraSerializer
from .models import Proveedor, Compra, DetalleCompra

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()

class CompraViewSet(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()

class DetalleCompraViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleCompraSerializer
    queryset =  DetalleCompra.objects.all()
