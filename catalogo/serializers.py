from rest_framework import serializers
from .models import Producto, PrecioProducto, Variacion, ProdcutoVariacion, Categoria
import datetime



class ProductoSerializer(serializers.ModelSerializer):
    ultima_modificacion = serializers.SerializerMethodField()
    propietario = serializers.ReadOnlyField(source='creador.username')
    class Meta:
        model = Producto
        fields = ('id','nombre','codigo','descripcion','imagen','tipo','ultima_modificacion','propietario','fecha','status')

    def get_ultima_modificacion(self,obj):
        return obj.last_modified.strftime("%Y-%m-%d %H:%M:%S")

class PrecioProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrecioProducto
        fields = '__all__'

class VariacionSerializer(serializers.ModelSerializer):
    creador = serializers.ReadOnlyField(source='creador.username')
    class Meta:
        model = Variacion
        fields = '__all__'

class ProdcutoVariacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdcutoVariacion
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','codigo','nombre','subname','peso','padre','hijos')
