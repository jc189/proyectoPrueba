from django.urls import path
from . import views

urlpatterns = [
    path('servicios/',views.serv,name='serv'),
    path('sesion/',views.inicio_de_sesion,name='inicio_de_sesion'),
    path('session/', views.session, name='session'),
    path('registro/',views.registro,name='registro'),
]

