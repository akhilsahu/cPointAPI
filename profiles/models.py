from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

class UserProfileManager(BaseUserManager):
	def create_user(self,phone_number,name,organisation,password=None):
		if not phone_number:
			raise ValueError('Phone Number is required field')	
		#phone_number=self.normalize_email(phone_number)
		user=self.model(phone_number=phone_number,name=name,organisation=organisation)
		user.set_password(password)
		user.save(using=self._db)
		return user			
		
	def create_superuser(self,phone_number,organisation,name,password):
		user=self.create_user(phone_number,name,organisation,password)
		user.is_superuser=True
		user.is_staff=True
		user.save(using=self._db)
		return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
	phone_number= PhoneNumberField( unique=True)
	name=models.CharField(max_length=255)
	organisation=models.CharField(max_length=255)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	added_by=models.ForeignKey(settings.AUTH_USER_MODEL)  
	objects=UserProfileManager()

	USERNAME_FIELD='phone_number'
	REQUIRED_FIELDS=['name','organisation']

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name
	def __str__(self):
		return self.name
