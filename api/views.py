from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from api import serializers
from api import models
from api import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permissions_classes=(permissions.UpdateOwnProfile,)

    def get_queryset(self):
        return models.UserProfile.objects.filter(username=self.request.user)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileTodoViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileTodoItemSerializer
    queryset=models.ProfileTodoItem.objects.all()
    permissions_classes=(
        permissions.UpdateOwnTodo,
        IsAuthenticated
    )

    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):
        return models.ProfileTodoItem.objects.filter(user_profile=self.request.user)
