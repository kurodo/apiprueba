from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'proveedor', ProveedorViewSet)
router.register(r'compra', CompraViewSet)
router.register(r'detalle_compra', DetalleCompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
