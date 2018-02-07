from django.db import models
import random


# Create your models here.


class SpaceMessage(models.Model):
    title = models.CharField(default='title', max_length=255)
    text = models.TextField(default='Text')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

# stringForToken = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 52^4= 7311616 возможных токенов


def maketokem():
    stringForToken = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    token = ''
    # задаем длинну ключа
    lenKey = int(4)
    # Вычеляем возможное кол-во ключей
    lenstringForToken = int(len(stringForToken))
    y = lenstringForToken ** lenKey
    # высчитываем оставшееся кол-во ключей
    getTokenList = TokenGenerator.objects.all()
    x = y - len(getTokenList)
    if x == 0:  # Проверка на наличие свободных ключей
        pass
    else:
        while token == '':
            for x in range(lenKey):
                randomKeyGenerate = random.choice(stringForToken)
                token = token + randomKeyGenerate
            a = TokenGenerator.objects.filter(tokens=token)
            if len(a) != 0:  # Проверка ключа на повторение
                token = ''
            else:
                return token


class TokenGenerator(models.Model):
    tokens = models.CharField(default=maketokem, max_length=255)
    status = models.BooleanField(default=False)

