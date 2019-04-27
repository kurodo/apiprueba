from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'venta', VentaViewSet)
router.register(r'detalle_venta', DetalleVentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
