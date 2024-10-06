from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:pk>", views.User_detail.as_view()),
    path("<int:pk>/tweets", views.User_tweets.as_view()),
]
