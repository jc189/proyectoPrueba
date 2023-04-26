from django.db import models


# Create your models here.

class usuarios(models.Model):
    num = models.CharField(max_length=5)

    def __str__(self) -> str:
        return str(self.num)