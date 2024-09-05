from django.db import models
from django.conf import settings


class Foto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='fotos')
    foto_url = models.URLField(max_length=255)
    description = models.TextField(blank=True, null=True)
    VISIBILITY_CHOICES = [
        ('public', 'Publico'),
        ('private', 'Privado'),
    ]
    visibilidad = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foto {self.id} de {self.user.username}"

class FotoMetadata(models.Model):
    foto = models.OneToOneField(Foto, on_delete=models.CASCADE, related_name='metadata')
    camara = models.CharField(max_length=100, blank=True, null=True)
    camara_modelo = models.CharField(max_length=100, blank=True, null=True)
    lente = models.CharField(max_length=100, blank=True, null=True)
    apertura = models.CharField(max_length=10, blank=True, null=True)
    velocidad_disparo = models.CharField(max_length=20, blank=True, null=True)
    iso = models.IntegerField(blank=True, null=True)
    distancia_focal = models.CharField(max_length=20, blank=True, null=True)
    capturada = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Metadata de la Foto {self.photo.id}"


class Comentario(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    foto = models.ForeignKey(
        Foto, on_delete=models.CASCADE, related_name='comentarios')
    texto_comentado = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario {self.user.username} en la Foto {self.foto.id}"
    

class Download(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='downloads')
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='downloads')
    descargado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Descarga de la Foto {self.photo.id} por {self.user.username}"
