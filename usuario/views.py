from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.views.generic import FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginView(FormView):
    template_name = 'accounts/login.html'  # La plantilla que se va a renderizar
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            auth_login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
            return self.form_invalid(form)


class MyAPIView(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}
        return Response(data, status=status.HTTP_200_OK)
