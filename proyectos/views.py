from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from proyectos.models import Usuario

# usuarios = """
# [
#     {
#         "username": "usuario1",
#         "password": "123"
#     },
#     {
#         "username": "usuario2",
#         "password": "abc"
#     },
#     {
#         "username": "usuario3",
#         "password": "aaa"
#     }
# ]
# """

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


# Path: /proyectos/login GET
# Response:
# {
#   "msg" : "" //Login correcto
# }
# {
#   "msg" : "Error en el login" //Login correcto
# }
def loginEndpoint(request, username, password):
    if request.method == "GET":
        # Peticion GET
        listaUsuarios = json.loads(usuarios)
        listaUsuariosFiltrada = list(
            filter(
                lambda x: x["username"] == username and x["password"] == password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada) > 0:
            respuesta = {
                "msg": ""
            }
            return HttpResponse(json.dumps(respuesta))
        else:
            respuesta = {
                "msg": "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))


# Path: /proyectos/login POST
@csrf_exempt
def loginPostEndpoint(request):  # formulario multipart para data pequeña o texto
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        listaUsuarios = json.loads(usuarios)
        listaUsuariosFiltrada = list(
            filter(
                lambda x: x["username"] == username and x["password"] == password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada) > 0:
            respuesta = {
                "msg": ""
            }
            return HttpResponse(json.dumps(respuesta))
        else:
            respuesta = {
                "msg": "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))


# path: /login-json
# Request:
# {
#   "username" : "usuario1",
#   "password" : "123"
# }

# Response:
# {
#   "msg": ""
# }
@csrf_exempt
def loginPostJsonEndpoint(request):  # para data mas estructurda
    if (request.method == "POST"):
        data = request.body
        usernameData = json.loads(data)

    username = usernameData["username"]
    password = usernameData["password"]

    # interactuamos con base de datos mediante el modelo usuario
    listaUsuariosFiltrada = Usuario.objects.filter(
        username=username, password=password
    )

    if len(listaUsuariosFiltrada) > 0:
        respuesta = {
            "msg": ""
        }
        return HttpResponse(json.dumps(respuesta))
    else:
        respuesta = {
            "msg": "Error en el login"
        }
        return HttpResponse(json.dumps(respuesta))
