from django.db import models


# Create your models here.
class usuario(models.Model):
	user = models.CharField(max_length=50)

	def __str__(self):
		return self.user

class tarea(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	proyecto = models.ForeignKey(usuario,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo + " - " + self.descripcion
