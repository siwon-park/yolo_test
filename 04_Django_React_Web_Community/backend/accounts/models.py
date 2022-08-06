from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=300)
    report = models.ManyToManyField('self', symmetrical=False, related_name='is_reported', blank=True)
    