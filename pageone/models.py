from django.db import models
from django.conf import settings
# Create your models here.

class news(models.Model):
    heading = models.CharField(max_length=100)
    desc = models.TextField()

User = settings.AUTH_USER_MODEL
class contact(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=150)
    city = models.CharField(max_length=40)
    def __str__(self): 
        return self.name 