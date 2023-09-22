from django.contrib.auth import logout, authenticate, login
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status, filters
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .permissions import *
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

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['name']
    search_fields = ['name']




    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryChooseAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get(self, request):
        user = self.request.user

        category = Category.objects.filter(user=user)
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        user = self.request.user
        category_id = self.request.data.get('category')
        try:
            category = Category.objects.get(id=category_id, user=user)

        except:
            raise serializers.ValidationError("Выбрана неверная категория!")
        serializer.save(user=user, category=category)


class TaskShowAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'deadline']
    search_fields = ['name', 'is_done']
    ordering_fields = ['name', 'is_done','deadline']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskChooseAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
