from django import forms


class crear_equipo_para_torneo(forms.Form):
    nombre= forms.CharField(max_length=20)
    localidad= forms.CharField(max_length=25)
    trofeos= forms.IntegerField()
    
class estadio_de_local(forms.Form):
    nombre= forms.CharField(max_length=20)
    ubicacion= forms.CharField(max_length=20)
    capacidad= forms.IntegerField()
    
class jugador_a_incluir(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    pais= forms.CharField(max_length=40)
    posicion= forms.CharField(max_length=30)