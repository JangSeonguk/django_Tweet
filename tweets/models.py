from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    """Tweet Model Definiton"""

    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload

    def total_likes(tweet):
        return tweet.likes.count()


class Like(CommonModel):
    """Like Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"'{self.tweet.payload}'"
