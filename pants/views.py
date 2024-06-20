
from django.shortcuts import render
from rest_framework import viewsets #creats set of views(pages) for me
from .models import Pants
from .serializers import PantsSerializer

class PantsViewSet(viewsets.ModelViewSet): #creates the view
    queryset = Pants.objects.all() #gets all instances from the model "Pants"
    serializer_class = PantsSerializer #serializes the data into JSON from model "Pants"