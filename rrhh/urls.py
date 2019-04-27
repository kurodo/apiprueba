from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'trabajador', TrabajadorViewSet)
router.register(r'salario', SalarioViewSet)
router.register(r'puesto', PuestoViewSet)
router.register(r'asistencia', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
