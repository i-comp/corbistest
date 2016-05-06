from django.db import models

# Max Length of CharField
MAX_LENGTH = 255


class Productos(models.Model):
    codigo = models.PositiveSmallIntegerField(unique=True)
    nombre = models.CharField(max_length=MAX_LENGTH)
    cantidad = models.PositiveSmallIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
