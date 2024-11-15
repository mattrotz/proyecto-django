from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Abogado

def abogados(request):
    abogados = Abogado.objects.all()
    return render(request, 'listas/lista-lawyer.html', {'abogados': abogados})

def registrar_abogado(request): 
    if request.method == 'POST': 
        nombre_abogado = request.POST.get('nombre') 
        correo_abogado = request.POST.get('correo') 
        contrasena_abogado = request.POST.get('contrasena') 
        documento_abogado = request.POST.get('documento')  
        telefono_abogado = request.POST.get('telefono') 
        
        Abogado.objects.create(nombre=nombre_abogado, correo=correo_abogado, contrasena=contrasena_abogado, documento=documento_abogado, telefono=telefono_abogado) 
        
        return redirect('lista-abogados') 

def editar_abogado(request, documento):
    abogado = Abogado.objects.get(documento=documento)
    return render(request,'edit/edicion_abogado.html',{'abogado':abogado})

def actualizar_abogado(request):
        nombre_abogado = request.POST.get('nombre') 
        correo_abogado = request.POST.get('correo') 
        contrasena_abogado = request.POST.get('contrasena') 
        documento_abogado = request.POST.get('documento')  
        telefono_abogado = request.POST.get('telefono')

        abogado = Abogado.objects.get(documento=documento_abogado) 

        abogado.nombre = nombre_abogado
        abogado.correo = correo_abogado
        abogado.contrasena = contrasena_abogado
        abogado.telefono = telefono_abogado
        abogado.documento = documento_abogado
        abogado.save()

        return redirect('/usuarios/lista-abogados')

def eliminar_abogado(request, documento_abogado):
    abogado = Abogado.objects.get(documento=documento_abogado)
    abogado.delete()

    return redirect('lista-abogados')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listas/lista-user.html', {'usuarios': usuarios})

def registrar_Usuario(request): 
    if request.method == 'POST': 
        nombre_usuarios = request.POST.get('nombre') 
        correo_usuarios = request.POST.get('correo') 
        contrasena_usuarios = request.POST.get('contrasena') 
        direccion_usuarios = request.POST.get('direccion')  
        telefono_usuarios = request.POST.get('telefono') 
        
        Usuario.objects.create(nombre_usuarios=nombre_usuarios, correo_usuarios=correo_usuarios, contrasena_usuarios=contrasena_usuarios, direccion_usuarios=direccion_usuarios, telefono_usuarios=telefono_usuarios) 
        
        return redirect('auth/lista-user.html') 

def actualizar_Usuario(request):
        nombre_usuarios = request.POST.get('nombre') 
        correo_usuarios = request.POST.get('correo') 
        contrasena_usuarios = request.POST.get('contrasena') 
        direccion_usuarios = request.POST.get('direccion')
        telefono_usuarios = request.POST.get('telefono')

        usuario = usuario.objects.get(correo=correo_usuarios) 

        usuario.nombre = nombre_usuarios
        usuario.correo = correo_usuarios
        usuario.contrasena = contrasena_usuarios
        usuario.telefono = telefono_usuarios
        usuario.direccion = direccion_usuarios
        usuario.save()

        return redirect('listas/lista-user.html')

def eliminar_Usuario(request, correo_usuarios):
    usuario = usuario.objects.get(correo=correo_usuarios)
    usuario.delete()

    return redirect('lista-Usuarios')