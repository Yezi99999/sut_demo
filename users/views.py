from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from .models import User
from .serializers import (UserRegistrationSerializer, UserLoginSerializer,
                          UserProfileSerializer, UserUpdateSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserProfileSerializer(user).data,
            'token': token.key,
            'message': '用户注册成功'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserProfileSerializer(user).data,
            'token': token.key,
            'message': '登录成功'
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_logout(request):
    logout(request)
    if hasattr(request.user, 'auth_token'):
        request.user.auth_token.delete()
    return Response({'message': '退出登录成功'})


@api_view(['GET', 'PUT'])
def user_profile(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'user': UserProfileSerializer(request.user).data,
                'message': '资料更新成功'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_list(request):
    if not request.user.is_staff:
        return Response({'error': '权限不足'}, status=status.HTTP_403_FORBIDDEN)

    users = User.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)