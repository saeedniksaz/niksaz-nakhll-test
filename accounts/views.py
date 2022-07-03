from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile


class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        ser_data = UserSerializer(users, many=True)
        return Response(ser_data.data)

class ProfileView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        ser_data = ProfileSerializer(profiles, many=True)
        return Response(ser_data.data)