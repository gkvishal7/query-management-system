from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.contrib.auth.base_user import BaseUserManager  
from django.utils import timezone
import datetime
from django.contrib.auth.base_user import BaseUserManager  
 
class userManager(BaseUserManager):   
    def create_user(self,username, email, password, **extra_fields):  
        if not email:  
            raise ValueError(_('The Email must be set'))  
        email = self.normalize_email(email)  
        user = self.model(username=username,email=email, **extra_fields)  
        user.set_password(password)  
        user.save()  
        return user  
  
    def create_superuser(self,username, email, password, **extra_fields):  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True)  
        if extra_fields.get('is_staff') is not True:  
            raise ValueError(_('Superuser must have is_staff=True.'))  
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError(_('Superuser must have is_superuser=True.'))  
        return self.create_user(username,email, password, **extra_fields)  
      

class user(AbstractBaseUser, PermissionsMixin):  
    username = models.CharField(max_length=45)
    email = models.EmailField(('email_address'), unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = [email,username]  
    objects = userManager()  
    def has_perm(self, perm, obj=None):  
        return True   
    def is_staff(self):    
        return self.staff  
    @property  
    def is_admin(self):    
        return self.admin  
    def __str__(self):  
        return self.email