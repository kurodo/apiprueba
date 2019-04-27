from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'almacen', AlmacenViewSet)
router.register(r'movimientos', MovimientoViewSet)
router.register(r'inventario', InventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
