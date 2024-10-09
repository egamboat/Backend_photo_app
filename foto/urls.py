from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'fotos', views.FotoView, basename='fotos')
router.register(r'comentario', views.ComentarioView, basename='comentario')

urlpatterns = [
    path("api/", include(router.urls)),
    path("documentacion/", include_docs_urls(title="Foto Api"))
]