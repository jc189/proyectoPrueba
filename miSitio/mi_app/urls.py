from django.urls import path
from . import views

urlpatterns = [
	path('',views.hello),
	path('par/<str:valor>',views.parametros),
	path('usuarios/<int:id>',views.usuarios),
	path('tareas/<int:id>',views.tareas),
]



