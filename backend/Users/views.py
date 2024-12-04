from rest_framework import viewsets, permissions
from django.urls import reverse_lazy
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer


class UserViewMixin(object):
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserViewSet(UserViewMixin, viewsets.ModelViewSet):
    pass

