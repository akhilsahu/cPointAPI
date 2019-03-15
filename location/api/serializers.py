from rest_framework import serializers
from location.models import Location


 
class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields=('id','area','user','latitude','longitude')

class LocationCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields=('id','area','latitude','longitude','user' )
		extra_kwargs={'user':{'read_only':True}}
