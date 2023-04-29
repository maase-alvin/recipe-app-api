"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, 
 BaseUserManager,
 PermissionsMixin )
# Create your models here.

class UserManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, password=None, **extra_fields):
        """
        Create, save and return a new user
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # user.set_password(password)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """
        Create and return a new superuser
        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports using email instead of username
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # can login
    is_staff = models.BooleanField(default=False) # staff user

    objects = UserManager()

    USERNAME_FIELD = 'email' # username field
    # REQUIRED_FIELDS = ['name'] # required fields

    def __str__(self):
        return self.email

    # def get_full_name(self):
    #     """
    #     Retrieve full name of user
    #     """
    #     return self.name

    # def get_short_name(self):
    #     """
    #     Retrieve short name of user
    #     """
    #     return self.name
