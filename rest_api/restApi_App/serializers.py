from rest_framework import serializers
from .models import *

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')



class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')