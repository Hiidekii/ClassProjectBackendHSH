from django.db import models

# Create your models here.

# creo modelo, hago migracion y aplico migracion
# se debe usar comando python manage.py makemigrations, python manage.py sqlmigrate proyectos 0001, python manage.py migrate


class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Equipo(models.Model):  # python manage.py makemigrations, python manage.py migrate
    EQUIPO_ESTADO = (
        ("A", "Activo"),
        ("I", "Inactivo")
    )
    nombre = models.CharField(max_length=50)
    anho = models.IntegerField(verbose_name="año", null=True)
    estado = models.CharField(max_length=1, choices=EQUIPO_ESTADO)

    def __str__(self):
        return self.nombre
