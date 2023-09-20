from django.contrib.auth import logout, authenticate, login
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import *


class RegisterAPIView(APIView):
    # serializer_class = RegistrationSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Успех": "Все прошло отлично!"}, status=status.HTTP_200_OK)
        return Response({"Ошибка": "("})


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"Ошибка": "Неверный логин или пароль!"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"Успех": "Все прошло отлично!"}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"good!": "good!"})


class CategoryAddShowAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)
