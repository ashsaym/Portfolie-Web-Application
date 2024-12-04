from rest_framework import serializers
from Users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"  # Use __all__ without quotes to include all model fields
