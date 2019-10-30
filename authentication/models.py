from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    Teacher = 1
    Student = 2

    USER_TYPE_CHOICES = (
        (1, 'Teacher'),
        (2, 'Student')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        return self.username
