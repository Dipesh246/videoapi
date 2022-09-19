from django.urls import path, include
from rest_framework.routers import DefaultRouter
from videostore import views
from .views import LogInView,RegisterView
router = DefaultRouter()
router.register(r'videos', views.VideoViewSet, basename='video')
# router.register(r'list-videos', views.VideoViewSet, basename='video')

urlpatterns = [
    path('',include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LogInView.as_view()),

]
