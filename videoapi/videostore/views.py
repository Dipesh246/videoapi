from rest_framework import viewsets, generics
from .models import video
from django_filters import rest_framework as filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
# from videostore.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .serializers import  LogInSerializer, VideoSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
# from django.http import JsonResponse
from django.contrib.auth import authenticate

class VideoFilter(filters.FilterSet):

  class Meta:
    model = video
    fields = {
      'video_name':['icontains'],
    
      'created_date':['iexact'],
    }

class VideoViewSet(viewsets.ModelViewSet):
  queryset = video.objects.all()
  serializer_class = VideoSerializer
  filterset_class = VideoFilter
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  filter_fields = ('video_size','created_date')

  # def perform_create(self, serializer):
  #   return super().perform_create(self, serializer)

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = video.objects.all()
  serializer_class = VideoSerializer
  # permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  




class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save() 

    refresh = RefreshToken.for_user(user)

    return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
  
class LogInView(CreateAPIView):
  serializer_class = LogInSerializer
  queryset = User.objects.all()

  def post(self,request, *args, **kwargs):
    data = request.data
    username = self.request.data.get('username')
    password = self.request.data.get('password')

    user = authenticate(username=username,password=password)
    print(user)

    if not user:
      return Response("Entered User/password is wrong.")

    refresh = RefreshToken.for_user(user)

    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    })