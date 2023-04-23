from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import usuario, tarea

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello!!!!!!</h1>")
    return render(request,"index.html")

def parametros(request,valor):
    return HttpResponse("Tu valor esta en consola %s" % valor)
    

def usuarios(request):
    #usr = list(usuario.objects.values())
    #return JsonResponse(usr,safe=False)
    return render(request, 'usuarios.html')

def tareas(request):
    #trs = get_object_or_404(tarea,id=id)
    #trs = tarea.objects.get()
    #return HttpResponse("Tarea: %s" % trs.titulo)
    return render(request, 'tareas.html')
