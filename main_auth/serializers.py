from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'last_name', 'role', 'password', 'password2')

    def validate(self, data):
        errors = []
        # user = CustomUser.objects.filter(name__iexact='qqq').first()
        # check = check_password(data['password'], user.password)
        # make_pass = make_password(data['password'])
        auth = authenticate(name=data['name'], password=data['password'])
        print(auth, 'auth')
        if data['password'] != data['password2']:
            errors.append({'password': 'password1 and password2 not matched'})

        # if user:
        #     errors.append({'user_name': 'this user name already exists'})

        if errors:
            raise serializers.ValidationError({'errors': errors})
        return data

    def create(self, validated_data):
        print(validated_data, 'start')
        validated_data.pop('password2')
        print(validated_data, 'finish')
        user = CustomUser.objects.create(**validated_data
            # email=validated_data['email'],
            # password=validated_data['password'],
            # role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
