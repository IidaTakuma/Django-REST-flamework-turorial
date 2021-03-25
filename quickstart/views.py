from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import (UserSerializer, GroupSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    Userの表示と編集を可能にするAPIエンドポイント
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Groupの表示と編集を可能にするAPIエンドポイント
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_classes = [permissions.IsAuthenticated]
