from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello!!!!!!</h1>")

def parametros(request,valor=""):
    return HttpResponse("Tu valor esta en consola %s" % valor)
