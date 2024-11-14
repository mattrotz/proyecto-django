from django.db import models

# Create your models here.

# Models_Usuario
class Usuario(models.Model):  
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)  
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nombre


# Models_Abogados
class Abogado(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True) 
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)  
    fecha_registro = models.DateTimeField(auto_now_add=True) 

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