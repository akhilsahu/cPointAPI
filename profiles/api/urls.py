from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .  import views
router=DefaultRouter()
router.register('profile',views.UserProfileViewSets,base_name='profile')
router.register('authOTP', views.UserAuthenticationAPIView ,base_name='auth')
router.register('login',views.UserLoginAPIView,base_name='login')
urlpatterns = [
	url(r'',include(router.urls)), 

]  