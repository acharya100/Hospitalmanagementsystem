from rest_framework import serializers
from appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    """custom appointment serializer fields"""
    class Meta:
        model = Appointment
        fields = [
            'id', 'patient', 'doctor',
            'department', 'booking',
            'appointment_date', 'appointment_time',
            'appointment_fee', 'appointment_description',
            'appointment_number', 'room_number',
            'created_at','updated_at'
        ]