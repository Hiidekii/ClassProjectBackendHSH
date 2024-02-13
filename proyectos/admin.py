from django.contrib import admin
from .models import Usuario, Equipo

# Register your models here.
# Para usar interfaz admin de django, python manage.py createsuperuser
admin.site.register(Usuario)
admin.site.register(Equipo)
