from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            'name',
            'city',
            'state',
            'slug',
            'image',
            'created_at',
            'updated_at'
        ]

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id','username')
