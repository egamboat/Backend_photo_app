from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Perfil(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    foto_perfil = models.URLField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Seguidor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='siguiendo')
    siguiendo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seguidores')

    class Meta:
        unique_together = ('user', 'siguiendo')

    def __str__(self):
        return f"{self.user.username} follows {self.siguiendo.username}"
