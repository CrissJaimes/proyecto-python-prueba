from django.shortcuts import render
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/base.html")

def creacion_de_equipo(request):

    if request.method == "POST":
        nombre_de_equipo = request.POST["nombre"]
        localidad_de_equipo = request.POST["localidad"]
        trofeos_del_equipo= request.POST["trofeos"]
        equipo = Equipo(nombre=nombre_de_equipo, localidad=localidad_de_equipo, trofeos=trofeos_del_equipo)
        equipo.save()


    return render(request, "AppCoder/equipo_crear.html")



def creacion_de_estadio(request):

    if request.method == "POST":
        nombre_del_estadio = request.POST["nombre"]
        localidad_del_estadio = request.POST["ubicacion"]
        capacidad_del_estadio= request.POST["capacidad"]
        estadio = Estadio(nombre=nombre_del_estadio, ubicacion=localidad_del_estadio, capacidad=capacidad_del_estadio)
        estadio.save()


    return render(request, "AppCoder/estadio_jugar.html")


def registrar_jugador(request):

    if request.method == "POST":
        nombre_del_jugador = request.POST["nombre"]
        apellido_del_jugador = request.POST["apellido"]
        posicion_del_jugador= request.POST["posicion"]
        jugador = Jugador(nombre=nombre_del_jugador, apellido=apellido_del_jugador, posicion=posicion_del_jugador)
        jugador.save()


    return render(request, "AppCoder/registrar_jugador.html")