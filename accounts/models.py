from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.contrib.auth.base_user import BaseUserManager  
from django.utils import timezone
from django.utils.translation import gettext as _

#Custom Model Manager 
class userManager(BaseUserManager):   
    def create_user(self,username, email, password, **extra_fields):  
        if not email:  
            raise ValueError(('The Email must be set'))  
        email = self.normalize_email(email)  
        user = self.model(username=username,email=email, **extra_fields)  
        user.set_password(password)  
        user.save()  
        return user  
  
    def create_superuser(self,username, email, password, **extra_fields):  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True)  
        return self.create_user(email=email,username=username,password=password,**extra_fields)
      
#Custom User Model
class user(AbstractBaseUser, PermissionsMixin):  
    username = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    objects = userManager() 
    USERNAME_FIELD = 'email'  
    EMAIL_FIELD='email'
    REQUIRED_FIELDS = ['username']  
    def has_perm(self, perm, obj=None):  
        return True   
    def __str__(self):  
        return self.email
    
    def getusername(self):  
        return self.username

