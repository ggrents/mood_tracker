from datetime import datetime

from rest_framework import serializers

from .models import *


# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email')
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         password = validated_data['password']
#         password2 = validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Пароли не совпадают'})
#
#         user.set_password(password)
#         user.save()
#         return user
#
#
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Task
        fields = ('name', 'is_done', 'deadline', 'category')
