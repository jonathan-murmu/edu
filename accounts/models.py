from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=True)
    course = models.ManyToManyField(Course, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)