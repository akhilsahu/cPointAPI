

from rest_framework.generics import (ListAPIView 
									,RetrieveAPIView 
									,UpdateAPIView
									,DestroyAPIView
									,CreateAPIView
									,RetrieveUpdateAPIView
									)
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from profiles.models import UserProfile
from rest_framework.permissions import ( AllowAny
										,IsAuthenticated
										,IsAdminUser
										,IsAuthenticatedOrReadOnly)
from rest_framework.authtoken.models import Token

class UserProfileViewSets(viewsets.ModelViewSet):
	serializer_class=serializers.UserProfileSerializer
	queryset=UserProfile.objects.all()

class UserAuthenticationAPIView(viewsets.ViewSet):
	permission_classes = [AllowAny]
	serializer_class=serializers.UserOTPSerializer
	queryset=UserProfile.objects.all()
	def update(self, request, pk=None):
		'''User to authenticate the phone number and send otp '''
		phone_number = request.data.get('phone_number', None)

		if phone_number:
			try:
				user=UserProfile.objects.get(phone_number=phone_number)
				otp=randint(1000, 9999)
				user.set_password(otp)
				user.save()
			except UserProfile.DoesNotExist:
				return Response({'message':'Mobile Number Does not exist'})	
			return Response({'OTP':otp})
		else:
			return Response({'message': 'Enter Mobile Number'})
			
class  UserLoginAPIView(viewsets.ViewSet):
	permission_classes = [AllowAny]
	serializer_class= AuthTokenSerializer
	def create(self,request):
		phone_number = request.data.get('phone_number', None)
		if phone_number:
 		 	try:
 		 		user=UserProfile.objects.get(phone_number=phone_number)
 		 		otp=randint(1000, 9999)
 		 		user.set_password(otp)
 		 		user.save()
 		 		token, created=Token.objects.get_or_create(user=user)
 		 		return Response({ 'token': token.key, 'user': user.pk  })
 		 	except UserProfile.DoesNotExist:
 		 		return Response({'message':'Mobile Number Does not exist'})
 		 	else:
 		 		return Response({'message': 'Enter Mobile Number'})
		

