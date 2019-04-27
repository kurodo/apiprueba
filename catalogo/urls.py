from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'producto', ProductoViewSet)
router.register(r'precio', PrecioProductoViewSet)
router.register(r'variacion', VariacionViewSet)
router.register(r'producto_variacion', ProdcutoVariacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('build/variaciones/<int:pk>/',CrearVariaciones.as_view())
]
urlpatterns += router.urls
