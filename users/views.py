from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from tweets.serializers import TweetSerializer
from tweets.models import Tweet
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT


class Users(APIView):
    def get(self, request):
        all_categories = User.objects.all()
        serializer = UserSerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                UserSerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class User_detail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = UserSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = UserSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                UserSerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class User_tweets(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user_tweets = Tweet.objects.filter(user=pk)
        serializer = TweetSerializer(user_tweets, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = UserSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                UserSerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)
