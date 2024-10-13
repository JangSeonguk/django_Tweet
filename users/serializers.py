from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        ]
