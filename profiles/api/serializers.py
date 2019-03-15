from rest_framework import serializers
from profiles.models import UserProfile


 
class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields=('id','phone_number','name','password','organisation')
		extra_kwargs={'password':{'write_only':True}}

	def create(self,validated_data):
		user=UserProfile(
		 		phone_number=validated_data['phone_number'],
		 		name=validated_data['name'],
		 		organisation=validated_data['organisation']
		 	)
		user.set_password(validated_data['password'])
		user.save()
		return user
class UserOTPSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields=('id', 'phone_number'  )
		
	def update(self,validated_data):
		user=UserProfile(
		 		phone_number=validated_data['phone_number'],
		 	 	)
		otp=random.randrange(0,4)
		user.set_password(otp)
		user.save()
		return user
class UserLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields=('id', 'phone_number' ,'password' )
		

 
	    