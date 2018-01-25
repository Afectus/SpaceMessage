from django.db import models
import random


# Create your models here.


class SpaceMessage(models.Model):
    title = models.CharField(default='title', max_length=255)
    text = models.TextField(default='Text')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

#stringForToken = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#52^4= 7311616 возможных токенов
    #while token == '' or token == TokenGenerator.objects.filter(tokens=token):
#def maketokem():
#    stringForToken = 'qw'
#    token = ''
#    while True:
#
#        if token == '' or token == TokenGenerator.objects.filter(tokens=token):
#            for x in range(1):
#                s = random.choice(stringForToken)
#                token = token + s
#                kek = TokenGenerator.objects.filter(tokens=token)
#                # print(TokenGenerator.objects.filter(tokens=token))
#                print('-' * 50)
#                print(kek)
#                print(s)
#                break
#        else:
#            return token

def maketokem():
    stringForToken = 'qw'
    token = ''
    for x in range(1):
        s = random.choice(stringForToken)
        token = token + s

    return token
class TokenGenerator(models.Model):
    tokens = models.CharField(default=maketokem, max_length=255, unique=True)
    status = models.BooleanField(default=False)
