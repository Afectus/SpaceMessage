from django.db import models
import random


# Create your models here.


class SpaceMessage(models.Model):
    title = models.CharField(default='title', max_length=255)
    text = models.TextField(default='Text')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
stringForToken = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
token = ''
for x in range(4):
    s = random.choice(stringForToken)
    token = token+s
    
class TokenGenerator(models.Model):
    tokens = models.CharField(default=token, max_length=255)
