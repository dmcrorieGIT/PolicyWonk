from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserModelSerializer
from .models import UserModel

class UserModelView(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()