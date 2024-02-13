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
