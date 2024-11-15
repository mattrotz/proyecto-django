
from django.urls import path
from .views import registrar_abogado, eliminar_abogado, editar_abogado, actualizar_abogado,abogados, usuarios, registrar_Usuario
from . import views

urlpatterns = [
    path('registro-abogados/', registrar_abogado, name='registro'),
    path('registro-usuarios/', registrar_Usuario, name='registro'),
    path('lista-abogados/', abogados, name='lista-abogados'),
    path('lista-Usuarios/', usuarios, name='usuarios'),
    path('lista-Usuarios/eliminar/<correo>', usuarios, name='usuarios'),
    path('actualizar_abogado/', actualizar_abogado, name='actualizar_abogado'),
    path('edicion-abogado/<documento>', editar_abogado, name='editar_abogados'),
    path('lista-abogados/eliminar/<documento>', eliminar_abogado, name='eliminar_abogado')
]

