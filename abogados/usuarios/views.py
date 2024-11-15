from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Abogado

def abogados(request):
    abogados = Abogado.objects.all()
    return render(request, 'listas/lista-lawyer.html', {'abogados': abogados})
def usuarios(request):
    #usuarios = Usuarios.objects.all()
    return render(request, 'listas/lista-user.html', {'usuarios': usuarios})


def registrar_abogado(request): 
    if request.method == 'POST': 
        nombre = request.POST.get('nombre') 
        correo = request.POST.get('correo') 
        contrasena = request.POST.get('contrasena') 
        documento = request.POST.get('documento')  
        telefono = request.POST.get('telefono') 
        
        Abogado.objects.create(nombre=nombre, correo=correo, contrasena=contrasena, documento=documento, telefono=telefono) 
        
        return redirect('lista-abogados') 

def eliminar_abogado(request, documento):
    abogado = Abogado.objects.get(documento=documento)
    abogado.delete()

    return redirect('lista-abogados')