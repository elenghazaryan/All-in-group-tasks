from rest_framework.serializers import ModelSerializer
from .models import Languages


class LanguageSerializers(ModelSerializer):
    class Meta:
        model = Languages
        fields = ['language', ]