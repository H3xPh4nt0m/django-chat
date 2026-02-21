from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    active_status = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
    def __str__(self):
        return self.email

