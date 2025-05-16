from django.db import models
from core.models import Usuario , Curso 

# Create your models here.

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=50)
    antiguedad = models.IntegerField()
    cursos = models.ManyToManyField(Curso,related_name="docentes")
