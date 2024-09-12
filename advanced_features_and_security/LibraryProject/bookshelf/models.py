from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
"ABSTRACT USER"
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username
    

"Create User Manager for Custom User Model (models.py):"

from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    model = CustomUser
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The username is required')
        if not email:
            raise ValueError('The email is required')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if password is None:
            raise ValueError('Superuser must have a password')

        return self.create_user(username, email, password, **extra_fields)

