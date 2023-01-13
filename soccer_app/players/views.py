from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PlayerModelSerializer
from .models import Player


class PlayerModelViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "goals"]
