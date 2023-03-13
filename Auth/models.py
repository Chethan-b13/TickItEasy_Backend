from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICE = (
        ('Organizers','Organizers'),
        ('Customer','Customer')
    )
    role = models.CharField(choices=ROLE_CHOICE,default='Customer',max_length=10)