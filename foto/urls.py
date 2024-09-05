from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('ver_foto/', views.ver_foto),
    
]
