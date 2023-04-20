from django.db import models
from django.http import HttpResponse

# Create your models here.

def prueba(request):
    return HttpResponse("<h1>Hello!!!</h1>")