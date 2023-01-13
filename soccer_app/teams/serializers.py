from rest_framework import serializers

from .models import Team


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "city",
            "goals_count",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "goals_count",
            "created_at",
            "updated_at",
        )
