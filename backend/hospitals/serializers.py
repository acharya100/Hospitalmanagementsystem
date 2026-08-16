from rest_framework import serializers
from hospitals.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'id', 'name','description',
            'email', 'phone_number',
            'address', 'shareholders',
            'established_date', 'opening_time',
            'opening_time','closing_time', 'is_open',
            'created_at', 'updated_at'
        ]