from django.shortcuts import render, redirect, get_object_or_404
from persona.models import Persona
from persona.forms import PersonaForm


# Vistas
# Agregar una nueva persona
def nuevaPersona(request):
    if request.method == "POST":
        formapersona = PersonaForm(request.POST)
        if formapersona.is_valid():
            formapersona.save()
            return redirect("ListadoPersonas")
    else:
        formapersona = PersonaForm()
    return render(request, "Agregar.html", {"formapersona": formapersona})


# Metodo para editar persona
def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect("ListadoPersonas")
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, "editarPersona.html", {"formapersona": formaPersona})


# EliminarPersona
def EliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect("ListadoPersonas")


# ConsultarPersonas
def DetallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "detallePersona.html", {"persona": persona})
