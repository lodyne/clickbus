from django.urls import path
from .views import (
    HomeView,
    APIEndpoints,
    APIGetSpecificPlace,
    APICreatePlace,
    APIEditPlace,
    APIListPlace,
)


urlpatterns = [
    # path('',HomeView.as_view(), name ='home'),
    path('',APIEndpoints.as_view(),name='overview'),
    path('places/',APIListPlace.as_view(), name='list'),
    path('places/new/',APICreatePlace.as_view(), name='create'),
    path('places/edit/<int:pk>/',APIEditPlace.as_view(), name='edit'),
    path('places/<int:pk>/',APIGetSpecificPlace.as_view(), name='detail')
]
