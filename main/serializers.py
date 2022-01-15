from .models import UUIDModel
from rest_framework import serializers


class UUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUIDModel
        fields = '__all__'
