"""wolapirest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from .views import *
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api-login/', obtain_jwt_token),
    path('catalogo/', include("catalogo.urls")),
    path('compra/', include("compra.urls")),
    path('inventario/', include("inventario.urls")),
    path('venta/', include("venta.urls")),
    path('rrhh/', include("rrhh.urls")),
    path('api-token-refresh/', refresh_jwt_token),
]
