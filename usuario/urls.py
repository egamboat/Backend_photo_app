from django.urls import path
from .views import LoginView, MyAPIView

urlpatterns = [
    path('login/', LoginView.as_view, name='login'),
    path('api/hello/', MyAPIView.as_view(), name='my_api_view'),
]
