from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User

from .serializers import RegisterCompanySerializer, UserSerializer, RegisterContractorSerializer



class RegisterCompanyView(generics.CreateAPIView):
    """POST /api/auth/register/ - register company and first admin comp"""
    serializer_class = RegisterCompanySerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class RegisterContractorView(generics.CreateAPIView):
    """POST /api/auth/register-contractor/ — регистрация исполнителя"""
    serializer_class = RegisterContractorSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )

class MeView(APIView):
    """GET /api/auth/me/ - this user"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)