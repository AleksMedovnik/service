from rest_framework import generics, viewsets
from .models import User, Category
from .serializers import UserSerializer, CatSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSerializer