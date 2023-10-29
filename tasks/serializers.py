from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

import json


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        depth = 0


class TasksImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        depth = 0




class TasksListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    

    def get_images(self, obj):
        # Only approved images can be displayed
        images = obj.images.all()
        return TasksImageSerializer(images, many=True).data


    class Meta:
        model = Tasks
        fields = ['id', 'user', 'title','images' ]
        depth = 0