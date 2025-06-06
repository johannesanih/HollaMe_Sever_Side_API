from django.db import models
from django.contrib.auth.models import AbstractUser

#user profile
# -- followers

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)