from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=[(
        'male', 'male'), ('female', 'female')])
    education_level = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
