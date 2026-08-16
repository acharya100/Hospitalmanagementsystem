from rest_framework import serializers
from prescriptions.models import Prescription, PrescriptionItem

class PrescriptionSerializer(serializers.ModelSerializer):
    """custom prescription serializer fields"""
    class Meta:
        model = Prescription
        fields = [
            'id', 'appointment', 'description',
            'patient', 'status', 'prescription_date',
            'prescription_time', 'total_price',
            'created_at','updated_at'
        ]

class PrescriptionItemSerializer(serializers.ModelSerializer):
    """custom prescription item serializer fields"""
    class Meta:
        model = PrescriptionItem
        fields = [
            'id', 'prescription', 'medicine_name',
            'unit_price', 'quantity'
            'created_at','updated_at'
        ]