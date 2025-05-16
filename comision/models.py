from django.db import models
from core.models import Usuario

# Create your models here.

class Comision(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    

class MiembroComision(models.Model):
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    rol = models.CharField(max_length=50)