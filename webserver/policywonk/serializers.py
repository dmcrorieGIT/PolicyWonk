# todo/serializers.py

from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('name', 'last_name')