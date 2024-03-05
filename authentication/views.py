from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (StudentResgistationSerializer, 
                          TeacherResgistationSerializer,
                          MyTokenObtainPairSerializer,)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = None

class StudentRegistrationView(BaseRegistrationView):
    serializer_class = StudentResgistationSerializer
    

class TeacherRegistrationView(BaseRegistrationView):
    serializer_class = TeacherResgistationSerializer


class LogoutView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
