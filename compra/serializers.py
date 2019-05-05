from rest_framework import serializers
from .models import Proveedor, Compra, DetalleCompra
from decimal import Decimal as D
from django.conf import settings

def formatiar(valor):
    valor = valor/100
    valor = D(valor)
    valor = "%s%0.2f" %(settings.FORMAT_CURRENCY, valor)
    return valor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    compras = serializers.StringRelatedField(many=True)
    format_total = serializers.SerializerMethodField()
    class Meta:
        model = Compra
        fields = ('id','fecha','tipo','proveedor','format_total','compras')

    def get_format_total(self,obj):
        return formatiar(obj.monto)


class DetalleCompraSerializer(serializers.ModelSerializer):
    format_precio = serializers.SerializerMethodField()
    format_total = serializers.SerializerMethodField()
    class Meta:
        model = DetalleCompra
        fields = ('id','precio','cantidad','unidad_compra','producto','format_precio','compra','format_total')

    def get_format_precio(self,obj):
        return formatiar(obj.precio)

    def get_format_total(self,obj):
        return formatiar(obj.total)
