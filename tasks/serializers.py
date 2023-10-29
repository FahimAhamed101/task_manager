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
        
        
class TasksUpdatedListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    
    original = TasksListSerializer()

    def get_user(self, obj):
        return UserListSerializer(obj.original.user).data

    def get_images(self, obj):
        # After approval, images with delete=False will remain
        images = obj.original.images.all()
        return TasksImageSerializer(images, many=True).data

    


class TasksDetailedSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    

    def get_images(self, obj):
        # Only approved images can be displayed
        images = obj.images.all()
        return TasksImageSerializer(images, many=True).data


    class Meta:
        model = Tasks
        fields = ['id','user',  'title', 'description','completed','priority','due_date','images']
        

class TasksCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
                       child=serializers.FileField(max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False), required=False, write_only=True)
    class Meta:
        model = Tasks
        fields = ['id','user',  'title', 'description','completed','priority','due_date','images']
        read_only_fields = ['id']
        depth = 0

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        title = validated_data.pop('title', None)
        completed = validated_data.pop('completed', None)
        priority = validated_data.pop('priority', None)
        due_date = validated_data.pop('due_date', None)
        tasks = super(TasksCreateSerializer, self).create(validated_data)

        # Images and variants are approved as default since this is initial create
        # This product does not show up until initial approval

        if images:
            images_data = [{"image": image, "tasks": tasks.id, "approved": True} for image in images]
            image_serializer = TasksImageSerializer(many=True, data=images_data, required=False)
            try:
                image_serializer.is_valid(raise_exception=True)
            except Exception as e:
                tasks.delete()
                raise ValidationError({"message": "Images are not allowed"})

  
        # Saving all serializers since there is no validation error
        if images:
            image_serializer.save()
        

        return tasks

    def validate(self, data):
        request = self.context.get("request", None)
        
        return data

class TasksUpdateSerializer(serializers.ModelSerializer):
    new_images = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False), default=[], required=False, write_only=True)
   
    class Meta:
        model = Tasks
        fields = ['id','user','new_images' , 'title', 'description','completed','priority','due_date','images',]
        
        read_only_fields = ()
        depth = 0

    def validate(self, data):
        new_images = data.pop("new_images", None)
        
        # draft_update_serializer = ProductDraftSerializer(draft, data=data)
        # draft_update_serializer.is_valid(raise_exception=True)
        # data.update({"draft_update_serializer": draft_update_serializer})

        if new_images:
            images_data = [{"image": image, "tasks": self.instance.id, "approved": None} for image in new_images]
            new_images_serializer = TasksImageSerializer(many=True, data=images_data, required=False)
            new_images_serializer.is_valid(raise_exception=True)
            data.update({"new_images_serializer": new_images_serializer})


        return data

    def patch(self, instance, validated_data):
        
        

        new_images_serializer = validated_data.pop('new_images_serializer', None)
        if new_images_serializer:
            new_images_serializer.save()

       
        

        return instance
    def put(self, instance, validated_data):
        
        

        new_images_serializer = validated_data.pop('new_images_serializer', None)
        if new_images_serializer:
            new_images_serializer.save()

       
        

        return instance
