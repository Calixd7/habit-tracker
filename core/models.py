from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from django.db.models import Q


class User(AbstractUser):
    pass

class HabitQuerySet(models.QuerySet):
    def for_user(self, user):
        if user.is_authenticated:
            habits = self.filter(Q(public=True) | Q(user=user))
        else:
            habits = self.filter(public=True)
        return habits

   

class Habit (models.Model):
    objects = HabitQuerySet.as_manager()
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target = models.IntegerField(blank=True, null=True)
    noun = models.CharField(max_length=255) 
    date = models.DateField(auto_now=True)
    public = models.BooleanField(default=True)


class Record (models.Model):
    outcome = models.IntegerField(blank=True, null=True)
    habit = models.ForeignKey(Habit, related_name = 'records', on_delete=models.CASCADE)
    date = models.DateField()
    # class Meta:
        # constraints = [ models.UniqueConstraint(fields=['habit', 'date'], name='unique_habit') ]

