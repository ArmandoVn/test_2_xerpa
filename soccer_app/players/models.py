from django.db import models

from general.models import TimestampMixin


class Player(TimestampMixin):
    name = models.CharField(max_length=200, verbose_name="Player name")
    goals = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players",
    )

    def __str__(self) -> str:
        return self.name
