from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    contact_information = models.CharField(max_length=200, verbose_name='Контактная информация', null=True)
    experience = models.CharField(max_length=200, verbose_name='Опыт', null=True)
    status = models.CharField(max_length=100, verbose_name='Статус', null=True)
    age = models.IntegerField(verbose_name='Возраст', null=True)