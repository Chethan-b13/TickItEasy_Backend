from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,role,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,role=role)
        user.set_password(password)
        user.save()

        return user
    

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
class User(AbstractUser,PermissionsMixin):

    objects = UserManager()
    email = models.EmailField(('email address'), unique=True)
    username=models.CharField(max_length=200,unique=False) # changes email to unique and blank to false
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    USERNAME_FIELD = 'email'
    ROLE_CHOICE = (
        ('Organizer','Organizer'),
        ('Customer','Customer')
    )
    role = models.CharField(choices=ROLE_CHOICE,max_length=10,default='Customer')