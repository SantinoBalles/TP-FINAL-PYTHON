from django.http import HttpResponse
from django.template import Template, Context

def saludar(request):
    return HttpResponse("<h1>mi primer mensaje desde django</h1>")

def mayor_de_edad(request, edad):
    if edad >= 18:
        return HttpResponse("<h1 style='color:green'>Usted es mayor de edad</h1>")
    else:
        return HttpResponse("<h1 style='color:red'>Usted es menor</h1>")


def probando_template(request):
    mi_html = open("C:/Users/tinob/OneDrive/Escritorio/TP-FINAL-PYTHON/Project1/Project1/plantilla/template.html")
    plantilla = Template( mi_html.read() )
    mi_html.close()

    mi_contexto = Context({"nombre":"Pepe"})

    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
