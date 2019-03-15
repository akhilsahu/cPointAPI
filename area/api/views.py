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
from area.models import Area
 

'''Fetch list all question '''
class AreasListApiView(ListAPIView):
	queryset=Area.objects.all()
	serializer_class=serializers.AreasSerializer

'''Fetch each question data using id'''
class AreasDetailAPIView(RetrieveAPIView):
	queryset=Area.objects.all()
	serializer_class = serializers.AreasSerializer 

'''Update data using id'''
class AreasUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Area.objects.all()
	serializer_class = serializers.AreasSerializer  
	#permission_classes=[ IsOwnerOrReadOnly]

'''Delete question data'''
class AreasDeleteAPIView(DestroyAPIView):
	queryset=Area.objects.all()
	serializer_class = serializers.AreasSerializer 
	#permission_classes=[IsOwnerOrReadOnly]


'''Ask new question '''
class AreasCreateAPIView(CreateAPIView):
	queryset=Area.objects.all()
	serializer_class = serializers.AreasCreateSerializer 
	#permission_classes=[IsAuthenticated]
	'''save user'''
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
