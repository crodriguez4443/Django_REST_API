from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers #allows GET and POST requests

router = routers.DefaultRouter()
router.register('pants', views.PantsViewSet) #pants is the url http//127.0.0.1:8000/pants

urlpatterns = [
    path('', include(router.urls)),
]
