from dataclasses import field
from rest_framework import serializers
# from .models import UserRegister
from .models import video
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip
import os
class VideoSerializer(serializers.ModelSerializer):
  amount = serializers.DecimalField(max_digits=5,decimal_places=2, read_only=True)
  additional_charges = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
  class Meta:
    model = video
    fields = "__all__"

  # def validate_Video(self,value):
  #   #print('value: ', value)
  #   video_size = value.size
  #   limit_byte_size = 1073741824
  #   video_type = value.name
  #   x = self.context['request'].FILES.get('Video')
  #   video_file_obj = VideoFileClip(x.temporary_file_path())
  #   if video_file_obj.duration >= 600:
  #     raise ValidationError('Please upload video of duration less than or equal to 10 min.')

  #   if not (video_type.endswith('.mp4') or video_type.endswith('.mkv')):
  #     raise ValidationError("Video type should be mp4 or mkv only")
  #   if(video_size>limit_byte_size):
  #       #converting into kb
  #     f= limit_byte_size/1024
  #       #converting into MB
  #     f=f/1024
  #       #converting into GB
  #     f=f/1024
  #     raise ValidationError("Video size should be under %s" % f)
  #   return value
    
  # def validate_amount(self,value):
  #   if(video_size<524288000):
  #     raise ValidationError("User should be charged not less then 5$ ")
  #   if(video_size>524288000):
  #     raise ValidationError("User should be charged not less then 12.5$ ")
  #   if(video_file_obj.duration>60 and video_file_obj.duration<378):
  #     raise ValidationError("User should additionally charged 12.5$")
  #   if(video_file_obj.duration>378):
  #     raise ValidationError("User should be charged additional 20$")  
    
    #return value
  def validate(self, value):
    video_size = value['Video'].size
    limit_byte_size = 1073741824
    video_type = value['Video'].name
    x = self.context['request'].FILES.get('Video')
    video_file_obj = VideoFileClip(x.temporary_file_path())
    if video_file_obj.duration >= 600:
      raise ValidationError('Please upload video of duration less than or equal to 10 secs.')

    if not (video_type.endswith('.mp4') or video_type.endswith('.mkv')):
      raise ValidationError("Video type should be mp4 or mkv only")
    if(video_size>limit_byte_size):
        #converting into kb
      f= limit_byte_size/1024
        #converting into MB
      f=f/1024
        #converting into GB
      f=f/1024
      raise ValidationError("Video size should be under %s" % f)

    if(video_size<524288000 and value['amount'] !=5):
      raise ValidationError("User should be charged not less then 5$ ")
    if(video_size>524288000 and value['amount'] !=12.5):
      raise ValidationError("User should be charged not less then 12.5$ ")
    if(video_file_obj.duration>60 and video_file_obj.duration<378 and value['additional_charges'] !=12.5):
      raise ValidationError("User should additionally charged 12.5$")
    if(video_file_obj.duration>378 and value['additional_charges'] != 20):
      raise ValidationError("User should be charged additional 20$")

    return super().validate(value)

# class UserSerializer(serializers.Serializer):
  

#   class Meta:
#     model = User
#     fields = ['id','username','email']


class RegisterSerializer(serializers.ModelSerializer):
  # username = serializers.CharField(max_length=100, write_only=True,style={'placeholder':'User Name'})
  # password = serializers.CharField(max_length=100, write_only=True, style={'input_type':'password','placeholder':'Password'})

  class Meta:
    model = User
    fields = ['id','username','email','password']
    extra_kwargs = {'password':{'write_only':True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
    return user

