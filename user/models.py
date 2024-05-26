from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, default='', verbose_name='شماره تلفن')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
