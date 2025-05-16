from django.db import models
from core.models import Usuario, Curso

# Create your models here.
class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField()
    cursos = models.ManyToManyField(Curso, related_name="estudiantes")