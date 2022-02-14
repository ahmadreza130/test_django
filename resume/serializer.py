from dataclasses import field
from rest_framework import serializers
from .models import Resume


class ResumeSer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
