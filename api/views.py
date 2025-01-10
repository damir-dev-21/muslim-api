from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .seriallizers import UserSerializer,PointSerializer
from .models import User,Point
import jwt
import datetime
import json

import base64
# Create your views here.


class RegisterUserView(APIView):

    def post(self, request):
        user = User()
        user.name = request.data['name']
        user.username = request.data['name']
        user.password = request.data['password']
        user.save()
        responce = Response()
        responce.data = {
            'message': 'success',
        }
        return responce




class GetPointsView(APIView):

    def post(self, request):
        point = Point()
        if request.data['title'] != None and request.data['title'] != "":
            point.title = request.data['title']
        point.latitude = request.data['latitude']
        point.longitude = request.data['longitude']
        point.save()
        responce = Response()
        responce.status_code = 200
        responce.data = {
            'status':True,
            
        }
        return responce


    def get(self, request):
        points = Point.objects.filter().all()
        pointsSerializers = PointSerializer(data=points, many=True)
        pointsSerializers.is_valid()

        responce = Response()
        responce.data = {
            'points': pointsSerializers.data,
        }
        return responce
    


class LoginView(APIView):

    def post(self, request):

        name = request.data['name']
        password = request.data['password']
        
        user = User.objects.filter(name=name).first()
       
        user.save()

        if user is None:
            raise AuthenticationFailed('User not found')

        if user.password != password:
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        serializer = UserSerializer(user)
        responce = Response()


        responce.set_cookie(key='jwt', value=token, httponly=True)

        responce.headers = {
            'jwt': token,
        }

        responce.data = {
            'status': True,
            'jwt': token,
            'user': serializer.data,
        }

        return responce
