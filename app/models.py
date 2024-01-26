from django.db import models

class Usuarios(models.Model):
    user = models.CharField(max_length=100, blank=False)
    senha = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.user


class Carros(models.Model):
    modelo = models.CharField(max_length=255, blank=False)
    marca = models.CharField(max_length=255, blank=True)
    complemento = models.CharField(max_length=255, blank=True)
    ano = models.IntegerField(blank=False)
    cor = models.CharField(max_length=255, blank=False)
    disponivel = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="uploads/", blank=False)
    
    def __str__(self):
        return self.modelo