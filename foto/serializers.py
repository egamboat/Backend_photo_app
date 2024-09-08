from rest_framework import serializers
from .models import Foto

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        #fields = ['id', 'user','titulo', 'foto_url', 'description', 'visibilidad', 'creacion', 'modificacion']
        fields = "__all__"