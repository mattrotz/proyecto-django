
from django.urls import path
from .views import registrar_abogado, eliminar_abogado, abogados, usuarios
from . import views

urlpatterns = [
    path('registro/', registrar_abogado, name='registro'),
    path('lista-abogados/', abogados, name='lista-abogados'),
    path('lista-usuarios/', usuarios, name='lista-usuarios'),
    path('lista-abogados/eliminar/<documento>', eliminar_abogado, name='eliminar_abogado')
]

