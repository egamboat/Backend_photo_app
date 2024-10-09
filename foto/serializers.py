from rest_framework import serializers
from .models import Foto, Comentario

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        #fields = ['id', 'user','titulo', 'foto_url', 'description', 'visibilidad', 'creacion', 'modificacion']
        fields = "__all__"

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"