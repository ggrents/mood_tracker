from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class TaskApiupdView(ListCreateAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskApiupdViewLst(ListAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskApiupdViewCrt(CreateAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIUpdate(UpdateAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIallfunc(RetrieveUpdateDestroyAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer