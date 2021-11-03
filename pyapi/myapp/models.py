from django.db import models

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=100)
    msg_id = models.IntegerField()
    message = models.CharField(max_length=1000)