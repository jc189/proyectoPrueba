from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def serv(request):
    return HttpResponse('Hi')


def inicio_de_sesion(request):
    return render(request,'inicio_de_session.html')