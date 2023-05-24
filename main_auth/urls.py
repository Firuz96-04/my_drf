from django.urls import path
from .views import index, RegisterUserSerializer
urlpatterns = [
    path('', index),
    path('register', RegisterUserSerializer.as_view())
]
