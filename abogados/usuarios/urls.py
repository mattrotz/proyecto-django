from django.urls import path
from .views import (
    registrar_abogado, eliminar_abogado, editar_abogado, actualizar_abogado, abogados,
    usuarios, registrar_usuario, editar_Usuario, actualizar_usuario, eliminar_usuario,
    Casos, crear_caso
)

urlpatterns = [
    # Rutas para Usuarios
    path('registro-usuarios/', registrar_usuario, name='registro_usuario'),
    path('lista-usuarios/', usuarios, name='lista_usuarios'),
    path('actualizar-usuarios/', actualizar_usuario, name='actualizar_usuario'),
    path('edicion-usuarios/<correo>/', editar_Usuario, name='editar_usuario'),
    path('eliminar-usuarios/<correo>/', eliminar_usuario, name='eliminar_usuario'),

    # Rutas para Abogados
    path('registro-abogados/', registrar_abogado, name='registro_abogado'),
    path('lista-abogados/', abogados, name='lista_abogados'),
    path('actualizar-abogado/', actualizar_abogado, name='actualizar_abogado'),
    path('edicion-abogado/<documento>/', editar_abogado, name='editar_abogado'),
    path('eliminar-abogado/<documento>/', eliminar_abogado, name='eliminar_abogado'),

    # Rutas para Casos
    path('lista-casos/', Casos, name='lista_casos'),
    path('crear-caso/', crear_caso, name='crear_caso'), 
]
