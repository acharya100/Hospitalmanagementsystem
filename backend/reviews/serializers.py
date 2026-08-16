from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """custom review serializer fields"""
    class Meta:
        model = Review
        fields =[
            'id', 'patient','hospital'
            'rating', 'comment',
            'created_at','updated_at'
        ]