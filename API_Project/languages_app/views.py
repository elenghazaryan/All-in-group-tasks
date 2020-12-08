from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Languages
from .serializers import LanguageSerializers

# Create your views here.


class AddLanguageCreateAPIView(CreateAPIView):
    serializer_class = LanguageSerializers

    def get_queryset(self, request):
        return Languages.object.create(lang=request.language)


class LanguagesListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializers
