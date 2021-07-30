from rest_framework import serializers 
from menu.models import (Plate, Group)

class PlateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plate
    fields = '__all__'
  
class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = '__all__'