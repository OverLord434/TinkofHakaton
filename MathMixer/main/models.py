from django.db import models
from users.models import User

class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stats')
    completed_trainings_number = models.IntegerField(default=0)
    completed_trainings_equation = models.IntegerField(default=0)
    completed_trainings_unequal = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    user_points = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.user.username}"
# Create your models here.
