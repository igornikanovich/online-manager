from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Student, Teacher, CustomUser


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
        model = CustomUser
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_teacher',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        is_teacher = validated_data.pop('is_teacher')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if not is_teacher:
            Student.objects.create(user_id=user.id)
        else:
            Teacher.objects.create(user_id=user.id)
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
            raise serializers.ValidationError('Unable to log in with provided credentials.')
        data['user'] = user
        return data
