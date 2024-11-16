from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Modelos de Usuario
class Usuario(models.Model):  
    nombre_usuarios = models.CharField(max_length=255)
    correo_usuarios = models.EmailField(unique=True)  
    contrasena_usuarios = models.CharField(max_length=128) 
    telefono_usuarios = models.CharField(max_length=15, blank=True, null=True)
    direccion_usuarios = models.TextField(blank=True, null=True)
    fecha_registro_usuarios = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        if self.contrasena_usuarios:
            self.contrasena_usuarios = make_password(self.contrasena_usuarios)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena_usuarios)

    def __str__(self):
        return self.nombre_usuarios


# Modelos de Abogado
class Abogado(models.Model):
    nombre_abogado = models.CharField(max_length=255)
    correo_abogado = models.EmailField(unique=True) 
    contrasena_abogado = models.CharField(max_length=128)
    documento_abogado = models.CharField(max_length=20, unique=True)
    telefono_abogado = models.CharField(max_length=15, blank=True, null=True)  
    fecha_registro_abogado = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        if self.contrasena_abogado:
            self.contrasena_abogado = make_password(self.contrasena_abogado)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena_abogado)

    def __str__(self):
        return self.nombre_abogado


# Modelo de Caso
class Caso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_resolucion = models.DateTimeField(null=True, blank=True)  # Campo para fecha de resolución

    def __str__(self):
        return f"Caso {self.id} - {self.estado}"
