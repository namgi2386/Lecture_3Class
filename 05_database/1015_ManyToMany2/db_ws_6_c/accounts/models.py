from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 이 유저가 구독한 유저 목록 
    subscription = models.ManyToManyField('self', symmetrical=False, related_name='subscriber' )
