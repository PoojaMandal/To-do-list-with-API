from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Task

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Customize the token response data
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom data to the response
        user = self.user
        data['user_id'] = user.id
        data['email'] = user.email

        return data

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
