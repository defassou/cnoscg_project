from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_president = models.BooleanField(default=False)
    is_superviseur = models.BooleanField(default=False)
    is_focal = models.BooleanField(default=True)
