from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Abogado, Caso


# Vista para mostrar la lista de abogados
def abogados(request):
    abogados = Abogado.objects.all()
    return render(request, 'listas/lista-lawyer.html', {'abogados': abogados})


# Registrar Abogado
def registrar_abogado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        documento= request.POST.get('documento')
        telefono = request.POST.get('telefono')

        Abogado.objects.create(
            nombre_abogado=nombre,
            correo_abogado=correo,
            contrasena_abogado=contrasena,
            documento_abogado=documento,
            telefono_abogado=telefono
        )
        
        return redirect('/usuarios/lista-abogados/')


# Editar Abogado
def editar_abogado(request, documento):
    abogado = Abogado.objects.get(documento_abogado=documento)
    return render(request, 'edit/edicion_abogado.html', {'abogado': abogado})


# Actualizar Abogado
def actualizar_abogado(request):
    if request.method == 'POST':  # Verifica que la solicitud sea POST
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo') 
        contrasena = request.POST.get('contrasena')
        documento = request.POST.get('documento')
        telefono = request.POST.get('telefono')

        abogado = Abogado.objects.get(documento_abogado=documento)

        abogado.nombre_abogado = nombre 
        abogado.correo_abogado = correo
        abogado.contrasena_abogado = contrasena
        abogado.telefono_abogado = telefono
        abogado.documento_abogado = documento
        abogado.save()

        return redirect('/usuarios/lista-abogados/')  # Redirige correctamente a la lista de abogados


# Eliminar Abogado
def eliminar_abogado(request, documento):
    abogado = Abogado.objects.get(documento_abogado=documento)
    abogado.delete()

    return redirect('/usuarios/lista-abogados/')  # Redirigir a la lista de abogados


# Vista para mostrar la lista de usuarios
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listas/lista-user.html', {'usuarios': usuarios})


# Registrar Usuario
def registrar_usuario(request):
    if request.method == 'POST':
        nombre_usuarios = request.POST.get('Nombre')
        correo_usuarios = request.POST.get('Correo')
        contrasena_usuarios = request.POST.get('Contrasena')
        direccion_usuarios = request.POST.get('Direccion')
        telefono_usuarios = request.POST.get('Telefono')

        Usuario.objects.create(
            nombre_usuarios=nombre_usuarios,
            correo_usuarios=correo_usuarios,
            contrasena_usuarios=contrasena_usuarios,
            direccion_usuarios=direccion_usuarios,
            telefono_usuarios=telefono_usuarios
        )


        return redirect('/usuarios/lista-usuarios/')  # Redirige correctamente a la lista de usuarios

def editar_Usuario(request, correo):
    usuario = Usuario.objects.get(correo_usuarios=correo)
    return render(request, 'edit/edicion_usuario.html', {'usuario': usuario})



# Actualizar Usuario
def actualizar_usuario(request):
    if request.method == 'POST':  # Verifica que la solicitud sea POST
        nombre = request.POST.get('Nombre')
        correo = request.POST.get('Correo')
        contrasena = request.POST.get('Contrasena')
        direccion = request.POST.get('Direccion')
        telefono = request.POST.get('Telefono')

        usuario = Usuario.objects.get(correo_usuarios=correo)

        usuario.nombre_usuarios = nombre
        usuario.correo_usuarios = correo
        usuario.contrasena_usuarios = contrasena
        usuario.telefono_usuarios = telefono
        usuario.direccion_usuarios = direccion
        usuario.save()

        return redirect('/usuarios/lista-usuarios/')  # Redirige correctamente a la lista de usuarios


# Eliminar Usuario
def eliminar_usuario(request, correo):
    usuario = Usuario.objects.get(correo_usuarios=correo)
    usuario.delete()

    return redirect('/usuarios/lista-usuarios/')  # Redirigir a la lista de usuarios

#ver lista de los casos
def Casos(request):
    casos = Caso.objects.all()
    return render(request, 'listas/lista-cases.html', {'casos': casos})


def crear_caso(request):
    if request.method == 'POST':
        nombre_abogado = request.POST.get('abogado')  # ID del abogado seleccionado
        nombre_usuarios = request.POST.get('usuario')  # ID del usuario seleccionado
        descripcion = request.POST.get('descripcion')
        
        try:
            abogado = Abogado.objects.get(id=nombre_abogado)
            usuario = Usuario.objects.get(id=nombre_usuarios)
        except Abogado.DoesNotExist:
            return HttpResponse("Abogado no encontrado", status=404)
        except Usuario.DoesNotExist:
            return HttpResponse("Usuario no encontrado", status=404)

        Caso.objects.create(
            usuario=usuario,
            abogado=abogado,
            descripcion=descripcion
        )

        return redirect('lista_casos')  # Cambia a la vista deseada
    else:
        abogados = Abogado.objects.all()  # Trae todos los abogados
        usuarios = Usuario.objects.all()  # Trae todos los usuarios
        return render(request, 'crear_caso.html', {'abogados': abogados, 'usuarios': usuarios})




