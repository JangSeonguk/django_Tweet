from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Elon Musk Filter"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Contain"),
            ("don't contain", "Don't contain"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        if word == "contain":
            return tweets.filter(payload__icontains="Elon Musk")
        elif word == "don't contain":
            return tweets.exclude(payload__icontains="Elon Musk")
        return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "total_likes",
    ]
    search_fields = [
        "payload",
        "user__username",
    ]
    list_filter = [
        WordFilter,
        "created_at",
    ]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "user",
        "tweet",
    ]

    search_fields = [
        "user__username",
    ]
    list_filter = ["created_at"]
