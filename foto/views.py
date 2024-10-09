from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets
from .models import Foto, Comentario
from .serializers import FotoSerializer,ComentarioSerializer

# Vista para crear una nueva foto

class FotoView(viewsets.ModelViewSet):
    serializer_class= FotoSerializer
    queryset= Foto.objects.all()

class ComentarioView(viewsets.ModelViewSet):
    serializer_class= ComentarioSerializer
    queryset= Comentario.objects.all()

    def editar():
        pass
