from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class User(AbstractUser):
    pass

class Habit (models.Model):
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target = models.IntegerField(blank=True, null=True)
    noun = models.CharField(max_length=255) 
    date = models.DateField(auto_now=True)



class Record (models.Model):
    outcome = models.IntegerField(blank=True, null=True)
    habit = models.ForeignKey(Habit, related_name = 'records', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    
    class Meta:
        constraints = [ 
         UniqueConstraint(fields=['habit', 'date'], name='unique_habit ')
         ]