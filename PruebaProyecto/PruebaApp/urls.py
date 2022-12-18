#creamos la direccion hacia el archivo views y su metodo
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),

]
