from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    foto = models.ImageField(upload_to="perfil/")
