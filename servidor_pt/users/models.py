from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Falta Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido']

    def __str__(self):
        return f'Usuario {self.nombre},{self.apellido}'
