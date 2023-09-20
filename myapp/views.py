from django.contrib.auth import logout, authenticate, login
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .permissions import IsCategoryOwner
from .serializers import *


class CategoryAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class CategoryShowAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryChooseAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCategoryOwner]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user = self.request.user
        category_id = self.request.data.get('category')
        try :
            category = Category.objects.get(id=category_id, user = user)

        except :
            raise serializers.ValidationError("Выбрана неверная категория!")
        serializer.save(user=user, category=category)


class TaskShowAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)