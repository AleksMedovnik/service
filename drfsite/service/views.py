from rest_framework import generics, viewsets
from .models import User, Category
from .serializers import UserSerializer, CatSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsAuthenticatedOrReadOnly, )

class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSerializer