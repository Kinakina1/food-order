from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser (AbstractUser):
    phone_number = models.CharField(max_length=11,verbose_name='شماره تماس')
    address = models.CharField(max_length=256,verbose_name='آدرس')
    points = models.IntegerField(default=0,verbose_name='امتیاز')

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    