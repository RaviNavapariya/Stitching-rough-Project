from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from log.managers import UserManager


class UserRole(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.name)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.PositiveIntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile_number']

    def __str__(self):  
        return str(self.email)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'