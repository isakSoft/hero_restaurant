from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """This class serializer transforms restaurant model instance to JSON format"""

    class Meta:
        """Mapping serializers fields with Model's ones"""
        model = Restaurant
        fields = ('id', 'name', 'opens_at', 'closes_at')
