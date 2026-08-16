from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """custom user serializer fields"""
    class Meta:
        model = User
        fields = [
            'id', 'name', 'bio', 'email',
            'phone_number', 'address',
            'date_of_birth', 'role'
        ]