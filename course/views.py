from rest_framework import generics

from course.models import Course
from course.serializers import CourseSerializer


class CourseAPIView(generics.ListAPIView):
    """Course Listing.

    A student should be able to view the available courses.
    """
    queryset = Course.objects.filter(is_available=True)
    serializer_class = CourseSerializer