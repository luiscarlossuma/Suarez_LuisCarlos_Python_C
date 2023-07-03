from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.Vproductos.as_view(), name='productos'),
    path('insertar/', views.insertar_producto, name='insertar')
]