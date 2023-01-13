from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TeamModelSerializer
from players.serializers import PlayerModelSerializer
from .models import Team


class TeamModelViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "city"]

    def teams_response(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, serializer_class=PlayerModelSerializer)
    def players(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        players = instance.players.all()
        return self.teams_response(players)
