import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_interviewer = models.BooleanField(default=False)


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    available_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return ""+str(self.user.id)+" -- "+self.user.username

