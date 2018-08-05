from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    # a course can have maximum 5 students enrolled.
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ('course_name',)