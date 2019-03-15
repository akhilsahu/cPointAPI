from rest_framework import serializers
from area.models import Area


 
class AreasSerializer(serializers.ModelSerializer):
	class Meta:
		model=Area
		fields=('id','areaName','user')

class AreasCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Area
		fields=('id','areaName','user' )
		extra_kwargs={'user':{'read_only':True}}
