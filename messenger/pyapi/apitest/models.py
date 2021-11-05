from django.db import models

# Create your models here.
class Message(models.Model):
    msgId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)