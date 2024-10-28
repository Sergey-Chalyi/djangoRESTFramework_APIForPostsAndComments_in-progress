from django.shortcuts import render
from rest_framework import generics

from user.models import User
from user.serializers import UserSerializer


# Create your views here.

class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



