from datetime import datetime

from rest_framework import serializers

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        user = kwargs['context']['request'].user
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)