from django.urls import path
from .views import verEquiposEndpoint, verEquiposPathParameterEndpoint, loginEndpoint, loginPostEndpoint

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    path("ver-equipos-path/<str:filtro>", verEquiposPathParameterEndpoint),
    path("login/<str:username>/<str:password>", loginEndpoint),
    path("login", loginPostEndpoint)
]
