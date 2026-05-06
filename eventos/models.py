from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=150)
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE) #Esta realacion es de uno a muchos, un usuario puede organizar varios eventos pero un evento solo puede tener un organizador

    def __str__(self):
        return self.nombre

class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #Esta relación es de uno a muchos, un usuario puede registrarse en varios eventos pero un evento puede tener varios registros
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE) #Esta relación es de uno a muchos, un evento puede tener varios registros pero un usuario solo puede registrarse en un evento
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.evento}"
