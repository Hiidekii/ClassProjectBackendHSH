from django.urls import path
from .views import verEquiposEndpoint, verEquiposPathParameterEndpoint

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    path("ver-equipos-path/<str:filtro>", verEquiposPathParameterEndpoint)
]
