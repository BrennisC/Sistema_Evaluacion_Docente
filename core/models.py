from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    permisos = models.TextField()

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    # Override the groups field with a custom related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='usuario_set',
        related_query_name='usuario',
    )
    
    # Override the user_permissions field with a custom related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuario_set',
        related_query_name='usuario',
    )

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    semestre = models.IntegerField()
    facultad = models.CharField(max_length=50)
    creditos = models.IntegerField()
    docente= models.ForeignKey('docente.Docente', on_delete=models.CASCADE)
    