# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    # first_name и last_name уже есть в AbstractUser
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
