from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'inicio/index.html',{})


def prueba(request):
    return HttpResponse("<h1>Hello!!!</h1>")