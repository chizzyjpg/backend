from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    return Response(UserSerializer(users, many=True).data)

def home(request):
    return render(request, "index.html")

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # notificación simple por correo
        send_mail(
            subject='Nuevo usuario creado',
            message=f"Se creó: {user.name} <{user.email}>",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_NOTIF_TO],
            fail_silently=True,  # para que no rompa si falla el SMTP en desarrollo
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
