from django.db import router
from django.urls import include, path
from .views import (
    HomeView,
    APIEndpoints,
    APIGetSpecificPlace,
    APICreatePlace,
    APIEditPlace,
    APIListPlace,
    APIUserList,
    APIUserDetail,
)

from .viewsets import (
    UserViewSet,
    PlaceViewSet
)

from rest_framework.routers import DefaultRouter, SimpleRouter

#* The DefaultRouter class automatically creates the API root view
router = DefaultRouter()

#* In contrary, the SimpleRouter doesn't create the API root view
# router = SimpleRouter()

router.register('users',UserViewSet, basename = 'users')
router.register('places', PlaceViewSet, basename = 'places')

urlpatterns = [
    path('',include(router.urls))
] 
# urlpatterns = [
#     # path('',HomeView.as_view(), name ='home'),
#     path('',APIEndpoints.as_view(),name='overview'),
#     path('places/',APIListPlace.as_view(), name='list'),
#     path('places/new/',APICreatePlace.as_view(), name='create'),
#     path('places/edit/<int:pk>/',APIEditPlace.as_view(), name='edit'),
#     path('places/<int:pk>/',APIGetSpecificPlace.as_view(), name='detail'),
#     # path('places/<slug:slug>',APIGetSpecificPlace.as_view(), name='detail')
#     path('users/',APIUserList.as_view(), name = 'users'),
#     path('users/<int:pk>/',APIUserDetail.as_view(), name = 'users-detail')
# ]
