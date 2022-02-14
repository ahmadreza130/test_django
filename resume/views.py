from ssl import VerifyMode
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view,authentication_classes
from django.contrib.auth.models import User
from .serializer import ResumeSer
from .models import Resume
from .verify import Verify
import jwt
import datetime
# Create your views here.


@api_view(['POST'])
@authentication_classes([Verify])
def create(req):
    seraializer = ResumeSer(data=req.data)
    seraializer.is_valid(raise_exception=True)
    seraializer.save()
    return Response(seraializer.data)


@api_view(['POST'])
@authentication_classes([Verify])
def edit(req):
    resume = Resume.objects.get(id=req.data['pk'])
    seraializer = ResumeSer(instance=resume, data=req.data)
    seraializer.is_valid(raise_exception=True)
    seraializer.save()
    return Response(seraializer.data)


@api_view(['DELETE'])
@authentication_classes([Verify])
def delete(req):
    resume = Resume.objects.get(id=req.data['pk'])
    resume.delete()
    return Response("resume deleted")


@api_view(['GET'])
@authentication_classes([Verify])
def get(req):
    resume = Resume.objects.all()
    serializer = ResumeSer(resume, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login(req):
    username = req.data['username']
    password = req.data['password']
    user = User.objects.filter(username=username).first()
    if user is None:
        raise AuthenticationFailed(
            "there is not an aacount with this userName")
    if not user.check_password(password):
        raise AuthenticationFailed("wrong password")
    token = jwt.encode({'id': user.id}, 'secretkey',
                       algorithm='HS256')
    return Response(token)
