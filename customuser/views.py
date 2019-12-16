from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()