from django.db import models    
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=2000)
class Message(models.Model):
    value = models.TextField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.TextField(max_length=1000000)
    room = models.TextField(max_length=1000000)
    
