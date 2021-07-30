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
  def get(self, request):
    groups = Group.objects.all()
    groupsSerializer = GroupSerializer(groups, many=True)
    return Response(groupsSerializer.data)


class PlateAPIView(APIView):
  def get(self, request):
    plates = Plate.objects.all()
    platesSerializer = PlateSerializer(plates, many=True)
    return Response(platesSerializer.data)
