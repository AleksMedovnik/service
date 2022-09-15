from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer