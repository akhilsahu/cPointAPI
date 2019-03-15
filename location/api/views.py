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
 
from . import serializers
from location.models import Location
 

'''Fetch list all question '''
class LocationListApiView(ListAPIView):
	queryset=Location.objects.all()
	serializer_class=serializers.LocationSerializer

'''Fetch each question data using id'''
class LocationDetailAPIView(RetrieveAPIView):
	queryset=Location.objects.all()
	serializer_class = serializers.LocationSerializer 

'''Update data using id'''
class LocationUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Location.objects.all()
	serializer_class = serializers.LocationSerializer  
	#permission_classes=[ IsOwnerOrReadOnly]

'''Delete question data'''
class LocationDeleteAPIView(DestroyAPIView):
	queryset=Location.objects.all()
	serializer_class = serializers.LocationSerializer 
	#permission_classes=[IsOwnerOrReadOnly]


'''Ask new question '''
class LocationCreateAPIView(CreateAPIView):
	queryset=Location.objects.all()
	serializer_class = serializers.LocationCreateSerializer 
	#permission_classes=[IsAuthenticated]
	'''save user'''
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
