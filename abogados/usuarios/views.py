from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Abogado
from django.views import View

def abogados(request):
    abogados = Abogado.objects.all()
    return render(request, 'lista-abogados/lista.html', {'abogados': abogados})

class AbogadoView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        documento = request.POST.get('documento')
        telefono = request.POST.get('telefono')

        Abogado.objects.create(nombre=nombre, correo=correo, documento=documento, telefono=telefono)
        return redirect('lista-abogados')

    def get(self, request):
        return render(request, 'auth/registrarse.html')
