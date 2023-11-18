from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexWeatherView.as_view(), name='index'),
    path('search_city/', search_city, name='search_name'),
    path('graph/<str:city_name>', graph_view, name='graph'),
]
