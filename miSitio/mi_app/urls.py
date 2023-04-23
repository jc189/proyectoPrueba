from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('par/<str:valor>',views.parametros),
	path('usuarios/',views.usuarios),
	path('tareas/',views.tareas),

]



