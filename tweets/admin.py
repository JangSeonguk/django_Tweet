from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "total_likes",
    ]

    def total_likes(self, tweet):
        return tweet.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
