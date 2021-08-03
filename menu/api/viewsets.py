from rest_framework import viewsets, mixins

from .serializers import (PlateSerializer, GroupSerializer)

from menu.models import (Plate, Group)


class PlateViewSet(
  mixins.CreateModelMixin, 
  mixins.RetrieveModelMixin, 
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  viewsets.GenericViewSet
):
  queryset = Plate.objects.all()
  serializer_class = PlateSerializer

class GroupViewSet(
  mixins.CreateModelMixin, 
  mixins.RetrieveModelMixin, 
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  viewsets.GenericViewSet
):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer