from django.contrib import admin

from .models import Player


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("team",)
    readonly_fields = ("created_at", "updated_at")
    list_display = (
        "name",
        "team",
        "id",
    )
