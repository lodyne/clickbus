from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Place
from .serializers import (
    PlaceSerializer,
    UserSerializer,
)

from rest_framework import viewsets

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer