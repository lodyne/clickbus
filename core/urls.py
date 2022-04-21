from django.urls import path
from .views import (
    APIOverview,
    HomeView,
    APICreatePlace,
    APIEditPlace,
    APIListPlace,
)


urlpatterns = [
    path('',HomeView.as_view(), name ='home'),
    path('api/',APIOverview.as_view(),name='overview'),
    path('api/list/',APIListPlace.as_view(), name='list'),
    path('api/create/',APICreatePlace.as_view(), name='create'),
    path('api/edit/<int:pk>/',APIEditPlace.as_view(), name='edit'),
    path('api/<int:pk>/',APIListPlace.as_view(), name='detail')
]
