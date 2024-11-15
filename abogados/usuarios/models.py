from django.db import models

# Create your models here.

# Models_Usuario
class Usuario(models.Model):  
    nombre_usuarios = models.CharField(max_length=255)
    correo_usuarios = models.EmailField(unique=True)  
    contrasena_usuarios = models.CharField(max_length=128) 
    telefono_usuarios = models.CharField(max_length=15, blank=True, null=True)
    direccion_usuarios = models.TextField(blank=True, null=True)
    fecha_registro_usuarios = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nombre


# Models_Abogados
class Abogado(models.Model):
    nombre_abogado = models.CharField(max_length=255)
    correo_abogado = models.EmailField(unique=True) 
    contrasena_abogado = models.CharField(max_length=128)
    documento_abogado = models.CharField(max_length=20, unique=True)
    telefono_abogado = models.CharField(max_length=15, blank=True, null=True)  
    fecha_registro_abogado = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.nombre
    

# Models_caso
class Caso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Caso {self.id} - {self.estado}"