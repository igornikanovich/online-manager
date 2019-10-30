from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    USER_UNIQUE_VALIDATOR = UniqueValidator(
        queryset=User.objects.all(),
        message='User with this username/email already exists.'
    )

    username = serializers.CharField(
        min_length=3,
        max_length=30,
        validators=[USER_UNIQUE_VALIDATOR]
    )
    email = serializers.EmailField(max_length=100, validators=[USER_UNIQUE_VALIDATOR])
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        max_length=64,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'user_type',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Wrong login or password.')
        data['user'] = user
        return data
