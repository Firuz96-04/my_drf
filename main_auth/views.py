from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins, generics
from .serializers import UserSerializer
from .models import CustomUser


# Create your views here.


@api_view(['GET'])
def index(request):
    return Response({'message': 'Ok'})


class RegisterUserSerializer(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.all()
        serial = UserSerializer(user, many=True)
        return Response({'data': serial.data})

    def post(self, request, *args, **kwargs):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response({'data': user.data})