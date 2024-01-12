from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Progress(models.Model):
    adhd_levels = ArrayField(models.CharField(max_length=100))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
