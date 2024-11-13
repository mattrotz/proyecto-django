from django.db import models

# Create your models here.

# Models_Usuario
class Usuario(models.Model): 
    IdUsuario = models.CharField(max_length=20,unique=True)
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_usuario} ({self.IdUsuario}) ({self.email})"


# Models_Abogados
class Abogados(models.Model):
    IdAbogado = models.CharField(max_length=20,unique=True)
    especialidad = models.CharField(max_length=100)
    nombre_abogado = models.CharField(max_length=100)
    email = models.CharField(max_length=50,unique=True)
    caso_actual = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.IdAbogado} ({self.nombre_abogado}) ({self.especialidad}) ({self.email}) ({self.caso_actual})"