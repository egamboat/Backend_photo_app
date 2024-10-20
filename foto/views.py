from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, viewsets
from .models import Foto, Comentario
from .serializers import FotoSerializer,ComentarioSerializer
from django.contrib.auth.models import User


class FotoView(viewsets.ModelViewSet):
    serializer_class= FotoSerializer
    queryset= Foto.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Foto.objects.all()
        return Foto.objects.filter(visibilidad='public')
    def get_queryset(self):
        # Si el usuario está autenticado, filtra las fotos por el usuario autenticado
        if self.request.user.is_authenticated:
            return Foto.objects.filter(user=self.request.user)
        # Si el usuario no está autenticado, solo retorna fotos públicas
        return Foto.objects.filter(visibilidad='public')
class ComentarioView(viewsets.ModelViewSet):
    serializer_class= ComentarioSerializer
    queryset= Comentario.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtrar comentarios por el ID de la foto.
        Si no se proporciona el ID de la foto, retorna todos los comentarios.
        """
        foto_id = self.request.query_params.get('foto_id')
        queryset = Comentario.objects.all()

        if foto_id:
            queryset = queryset.filter(foto_id=foto_id)
            
        queryset = queryset.select_related('user')
        return queryset

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        user = User.objects.get(id=user_id)
        serializer.save(user=user)

class UserFotoView(viewsets.ModelViewSet):
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Foto.objects.filter(user=self.request.user)
