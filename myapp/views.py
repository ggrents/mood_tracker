from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import *


class ShowAddCategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChosenCategoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





class AddTasksAPIView(CreateAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def perform_create(self, serializer):

        user = self.request.user
        serializer.save(user=user)


class ShowTasksAPIView(ListAPIView) :
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user_id=user_id)

    serializer_class = TaskSerializer
