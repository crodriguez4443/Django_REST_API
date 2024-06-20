from rest_framework import serializers
from .models import Pants

class PantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pants
        fields = ['id','name', 'url','fabric', 'quantity', 'four_way_stretch', 'price']