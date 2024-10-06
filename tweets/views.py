from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT


class Tweets(APIView):
    def get(self, request):
        all_categories = Tweet.objects.all()
        serializer = TweetSerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                TweetSerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


class Tweet_detail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = TweetSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = TweetSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                TweetSerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
