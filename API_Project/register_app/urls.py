from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register'),
]