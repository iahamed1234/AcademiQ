from django.db import models
# Code I wrote
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
# Custom User Manager for handling user creation
class CustomUserManager(BaseUserManager): # Before Custom User to allow properties to be available
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Custom User Model to include user information
class customUser(AbstractUser):
    real_name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    objects = CustomUserManager()


#End of Code I wrote