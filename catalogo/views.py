from django.shortcuts import render

from .serializers import ProductoSerializer, PrecioProductoSerializer, VariacionSerializer, ProdcutoVariacionSerializer
from .models import Producto, PrecioProducto, Variacion, ProdcutoVariacion

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets,status

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(status=True).order_by('-last_modified')

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)

class PrecioProductoViewSet(viewsets.ModelViewSet):
    serializer_class = PrecioProductoSerializer
    queryset = PrecioProducto.objects.all()

class VariacionViewSet(viewsets.ModelViewSet):
    serializer_class = VariacionSerializer
    queryset = Variacion.objects.all()

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)

class ProdcutoVariacionViewSet(viewsets.ModelViewSet):
    serializer_class = ProdcutoVariacionSerializer
    queryset = ProdcutoVariacion.objects.all()

class CrearVariaciones(APIView):
    def get(self, request, pk, format=None):
        producto = Producto.objects.filter(id = pk)
        if producto:
            producto[0].crear_variaciones(request.user)
        return Response(status=status.HTTP_201_CREATED)
