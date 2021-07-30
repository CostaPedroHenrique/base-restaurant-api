from rest_framework import viewsets

from .serializers import (PlateSerializer, GroupSerializer)

from menu.models import (Plate, Group)


class PlateViewSet(viewsets.ModelViewSet):
  queryset = Plate.objects.all()
  serializer_class = PlateSerializer

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer