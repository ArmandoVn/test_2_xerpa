from django.db import models
from django.utils import timezone


# Create your models here.
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now, help_text="Auto created at"
    )
    updated_at = models.DateTimeField(auto_now=True, help_text="Auto updated at")

    class Meta:
        abstract = True
