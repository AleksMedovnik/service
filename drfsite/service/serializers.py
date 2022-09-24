from rest_framework import serializers
from .models import User, Category


class UserSerializer(serializers.ModelSerializer):
    manager = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'