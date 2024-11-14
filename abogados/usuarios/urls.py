
from django.urls import path
from .views import AbogadoView, abogados

urlpatterns = [
    path('registro/', AbogadoView.as_view(), name='registro'),
    path('lista-abogados/', abogados, name='lista-abogados'),
]

