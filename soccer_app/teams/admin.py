from django.contrib import admin

from .models import Team


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    readonly_fields = ("goals_count", "created_at", "updated_at")
    list_display = (
        "name",
        "city",
        "id",
    )
