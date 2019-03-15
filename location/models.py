from django.db import models
 
from django.conf import settings

# Create your models here.
class Location(models.Model):
    name =models.TextField()
    area = models.ForeignKey('area.Area', on_delete=models.CASCADE)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL )
    def __str__(self):
        return self.name 

