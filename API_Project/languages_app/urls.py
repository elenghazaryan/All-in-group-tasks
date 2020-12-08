from django.urls import path
from .views import LanguagesListAPIView, AddLanguageCreateAPIView


urlpatterns = [
    path('languages/', LanguagesListAPIView.as_view(), name='languages'),
    path('add_language/', AddLanguageCreateAPIView.as_view(), name='add_language'),
]