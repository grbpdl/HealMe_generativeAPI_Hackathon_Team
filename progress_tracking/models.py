from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class  ADHDProgress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    response_date = models.DateField()
    score = models.IntegerField()

    class Meta:
        ordering=['user','response_date']
