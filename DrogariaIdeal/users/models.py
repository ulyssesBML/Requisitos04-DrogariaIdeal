from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    endereco = models.CharField(max_length=250)
