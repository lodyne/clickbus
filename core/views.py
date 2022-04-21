from django.shortcuts import render
from django.views.generic import TemplateView


from .models import Place
from .serializers import PlaceSerializer

from rest_framework import  generics
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# def home(request):
#     return render(request,'core/home.html')

class HomeView(TemplateView):
    template_name = "core/home.html"

class APIOverview(APIView):
    def get(self, request, format=None):
        api_urls = {
            'List Place': 'list/',
            'Get Specific Place': 'detail/<int:pk>/',
            'Create Place':'create/',
            'Edit Place':'edit/<int:pk>',
        }
        
        return Response(api_urls)

#* A view API to create a place
class APICreatePlace(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

#* A view API to edit a place 
class APIEditPlace(generics.RetrieveUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

#* A view API to list place and filter by name 
class APIListPlace(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

#* A view API to get a specific place 
class APIGetSpecificPlace(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

