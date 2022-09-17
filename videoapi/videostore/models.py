from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

# Create your models here.
class video(models.Model):
  
  Video = models.FileField(upload_to='videoapi/video')
  # s = Video.size
  video_name = models.CharField(max_length=50)
  video_discription = models.TextField()
  # video_size = models.DecimalField(default=0, decimal_places=2, max_digits=12)
  created_date = models.DateTimeField(auto_now=timezone.now)
  types = [('.mp4','MPEG-4'),('.mov','MOV')]
  video_formate = models.CharField(max_length=5,choices=types,default='.mp4')

# class UserRegister(models.Model):

#   first_name= models.CharField(max_length=20)
#   last_name = models.CharField(max_length=20)
#   user_name= models.CharField(max_length=20)
#   email = models.EmailField(_(""), max_length=254)
#   password = models.CharField(max_length=20, style = {'input_type':'password','placeholder':'Password'})
#   confirm_password = models.CharField(max_length=20, style = {'input_type':'password','placeholder':'Confirm Password'})

  

