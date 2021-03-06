from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from .models import Place
from .serializers import (
    PlaceSerializer,
    UserSerializer,
)

from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
# def home(request):
#     return render(request,'core/home.html')

class HomeView(TemplateView):
    template_name = "core/home.html"

#* A view API to list all endpoints
class APIEndpoints(APIView):
    '''
        This view displays all endpoints and helps to document my API. 
    '''
    def get(self, request, format=None):
        api_urls = {
            'GET - List Place': reverse('list',request=request,format=format),
            # 'GET - Get Specific Place': reverse('detail',request=request,format=format),
            # 'POST - Create Place': reverse('create',request=request,format=format),
            # 'PUT - Edit Place': reverse('edit',request=request,format=format),
        }
        
        return Response(api_urls)

        # return Response({
        #     'places': reverse('list',request=request,format=format)
        # })

#* A view API to list place and filter by name 
class APIListPlace(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    # filter_field = ('name','city')


#* A view API to create a place
class APICreatePlace(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


#* A view API to edit a place 
class APIEditPlace(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


#* A view API to get a specific place 
class APIGetSpecificPlace(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class APIUserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
