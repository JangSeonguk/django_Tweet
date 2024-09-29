from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class PerkAdmin(admin.ModelAdmin):
    pass
