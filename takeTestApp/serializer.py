from rest_framework import serializers
from .models import Registration, TestCenter

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class TestCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCenter
        fields = '__all__'