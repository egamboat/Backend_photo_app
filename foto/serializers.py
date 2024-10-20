from rest_framework import serializers
from .models import Foto, Comentario

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        #fields = ['id', 'user','titulo', 'foto_url', 'description', 'visibilidad', 'creacion', 'modificacion']
        fields = "__all__"

class ComentarioSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.SerializerMethodField()

    class Meta:
        model = Comentario
        fields = ['id', 'texto_comentado', 'creacion', 'foto', 'nombre_usuario', 'user']
        read_only_fields = ['creacion', 'nombre_usuario']

    def get_nombre_usuario(self, obj):
        return obj.user.username
