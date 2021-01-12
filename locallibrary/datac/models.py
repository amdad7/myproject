from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class User(models.Model):
    user_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')
    user_status=models.IntegerField(default=1)
    password=models.CharField(max_length=40,default="12345")
    def __str__(self):
        return (self.user_text)
