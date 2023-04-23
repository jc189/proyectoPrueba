from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import usuario, tarea

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello!!!!!!</h1>")

def parametros(request,valor=""):
    return HttpResponse("Tu valor esta en consola %s" % valor)


def usuarios(request,id):
    usr = list(usuario.objects.values())
    return JsonResponse(usr,safe=False)

def tareas(request,id):
    trs = get_object_or_404(tarea,id=id)
    return HttpResponse("Tarea: %s" % trs.titulo)
