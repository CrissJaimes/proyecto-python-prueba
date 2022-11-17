from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("registrar/equipos/", creacion_de_equipo, name="registro_de_equipo"),
    path("elegir/estadio/", creacion_de_estadio, name="eleccion_de_estadio"),
    path("registrar/jugador/", registrar_jugador, name="registro_de_jugador"),
    path("busqueda/estadio/", buscar_estadio, name="busqueda_estadio"),
    
]