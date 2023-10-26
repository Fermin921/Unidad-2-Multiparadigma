from django.shortcuts import render
from persona.models import Persona


def index(request):
    return render(request, "Bienvenido.html")


def indexPersona(request):
    personas = Persona.objects.order_by("id")

    return render(request, "IndexPersona.html", {"personas": personas})


# Create your views here.
