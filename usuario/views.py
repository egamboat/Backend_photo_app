from rest_framework.decorators import api_view ,authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework. permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
def login(request):
    user= get_object_or_404(User, username=request.data['username'])
    
    if not user .check_password(request.data['password']):
        return Response({"error": "Contraseña Inválida"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, _= Token.objects.get_or_create(user= user)
    serializer = UserSerializers(instance=user)

    return Response({"token":token.key, "user": serializer.data}, status= status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializers(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save(commit=False)  # No guarda aún en la base de datos
        user.set_password(serializer.validated_data['password'])  # Encripta la contraseña
        user.save()  # Ahora guarda el usuario con la contraseña encriptada
        
        # Crear token de autenticación
        token = Token.objects.create(user=user)

        return Response({
            'token': token.key, 
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def reset_password(request):
    username_or_email = request.data.get('username_or_email')
    new_password = request.data.get('new_password')

    if not username_or_email or not new_password:
        return Response({"error": "Es necesario que coloque su Usuario o Correo y la nueva contraseña."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username=username_or_email)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    user.set_password(new_password)
    user.save()

    return Response({"message": "Reseteo de contraseña realizado."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    
    return Response("Está logueado{}".format(request.user.username), status=status.HTTP_200_OK)



