from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .api.serializers import (
  GroupSerializer,
  PlateSerializer
)

from .models import Group, Plate 

# Create your views here.

class GroupAPIView(APIView):
  '''
    Api de grupos de pratos
  '''
  serialezer_class = GroupSerializer
  def get(self, request):
    groups = Group.objects.all()
    groupsSerializer = GroupSerializer(groups, many=True)
    return Response(groupsSerializer.data)


class PlateAPIView(APIView):
  '''
    Api de pratos
  '''

  serialezer_class = PlateSerializer
  def get(self, request):
    plates = Plate.objects.all()
    platesSerializer = PlateSerializer(plates, many=True)
    return Response(platesSerializer.data)
