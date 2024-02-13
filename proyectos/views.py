from django.shortcuts import render
from django.http import HttpResponse
import json

equipos = """
[
    {
        "nombre": "equipo1",
        "integrantes": [
            {
                "nombre": "N1",
                "codigo": "20202323"
            },
            {
                "nombre": "N2",
                "codigo": "20224533"
            }
        ]
    },
    {
        "nombre": "Equipo 2",
        "integrantes": [
            {
                "nombre": "N3",
                "codigo": "20202323"
            },
            {
                "nombre": "N4",
                "codigo": "20224533"
            }
        ]
    },
    {
        "nombre": "Equipo 3",
        "integrantes": [
            {
                "nombre": "N5",
                "codigo": "20202323"
            },
            {
                "nombre": "N6",
                "codigo": "20224533"
            }
        ]
    }
]
"""

# Create your views here.


def verEquiposEndpoint(request):  # query parameter
    if request.method == "GET":
        # Es una peticion de tipo GET
        # Obtenemos query parameter llamdo nombre
        nombreFiltro = request.GET.get("nombre")
        print(nombreFiltro)

        # def filtro(equipo):
        #     return equipo["nombre"].lower() == nombreFiltro       filtro, listaEquipos)

        listaEquipos = json.loads(equipos)
        listaEquiposFiltrada = list(
            filter(
                lambda x: x["nombre"].lower() == nombreFiltro,
                listaEquipos
            )
        )
        return HttpResponse(json.dumps(listaEquiposFiltrada))

    return HttpResponse(equipos)


def verEquiposPathParameterEndpoint(request, filtro):
    if request.method == "GET":
        # Es una peticion de tipo GET
        # Obtenemos query parameter llamdo nombre
        nombreFiltro = filtro

        # def filtro(equipo):
        #     return equipo["nombre"].lower() == nombreFiltro       filtro, listaEquipos)

        listaEquipos = json.loads(equipos)
        listaEquiposFiltrada = list(
            filter(
                lambda x: x["nombre"].lower() == nombreFiltro,
                listaEquipos
            )
        )
        return HttpResponse(json.dumps(listaEquiposFiltrada))

    return HttpResponse(equipos)
