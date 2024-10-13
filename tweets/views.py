from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Tweets(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_categories = Tweet.objects.all()
        serializer = TweetSerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save(user=request.user)
            return Response(
                TweetSerializer(new_tweet).data,
            )
        else:
            return Response(serializer.errors)


class Tweet_detail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied("You don't have permission to edit this tweet.")
        serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_tweet = serializer.save()
            return Response(
                TweetSerializer(update_tweet).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied("You don't have permission to delete this tweet.")
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
