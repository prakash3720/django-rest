from rest_framework import serializers
from api import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields=('id','username','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        user=models.UserProfile.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileTodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProfileTodoItem
        fields=('id','user_profile','todo','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}
