from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .  import views

router=DefaultRouter()
#router.register('areas',views.AreasListApiView.as_view(),base_name='areas')

urlpatterns = [
	url(r'',include(router.urls)),

	url(r'^$',views.LocationListApiView.as_view(), name='list'),
    url(r'^create/$',views.LocationCreateAPIView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',views.LocationDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$',views.LocationUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$',views.LocationDeleteAPIView.as_view(), name='delete'),


	]  