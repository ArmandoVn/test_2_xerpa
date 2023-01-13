from django.db import models
from django.db.models import Sum

from general.models import TimestampMixin


class Team(TimestampMixin):
    name = models.CharField(max_length=200, verbose_name="Team name")
    city = models.CharField(max_length=200, verbose_name="City name")

    def __str__(self) -> str:
        return self.name

    @property
    def goals_count(self):
        return self.players.aggregate(Sum("goals"))["goals__sum"]
