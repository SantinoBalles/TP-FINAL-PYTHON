from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=235432)
    curso.save()
    texto = f"Se guardo en la BD del curso: {curso.nombre} {curso.camada}" 
    return HttpResponse(texto)