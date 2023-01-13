from rest_framework.serializers import ModelSerializer

from .models import Player


class PlayerModelSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = (
            "id",
            "name",
            "goals",
            "team",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
