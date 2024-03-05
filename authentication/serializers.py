from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}


class StudentResgistationSerializer(UserRegistrationSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_student = True
        instance.save()
        return instance
    
class TeacherResgistationSerializer(UserRegistrationSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_teacher = True
        instance.save()
        return instance
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_teacher'] = user.is_teacher
        return token
    