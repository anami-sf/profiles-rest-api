from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Create a user profile manager to work with the django build-in admin 

    # UserProfileManager is devined ????
    objects = UserProfileManager()

    # Override the username filed used to authenticate users

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


    
