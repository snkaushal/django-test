from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from customuser import permissions
from . import serializers
from . import models
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedItemViewSet(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)
  serializer_class = serializers.UserProfileFeedItemSerializer
  queryset = models.UserProfileFeedItem.objects.all()
  permission_classes = (
    permissions.UpdateOwnStatus,
    IsAuthenticated
 )

  def perform_create(self, serializer):
    serializer.save(user_profile = self.request.user)
