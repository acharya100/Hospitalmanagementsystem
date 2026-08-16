from rest_framework import serializers
from departments.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    """custom department serializer fields"""
    class Meta:
        model = Department
        fields = [
            'id', 'name','description',
            'doctors', 'hospital', 'is_available',
            'created_at','updated_at'
        ]