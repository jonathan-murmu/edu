from django.db.models import Count
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from course.constants import MAX_STUDENTS
from course.models import Course
from course.serializers import CourseSerializer


class CourseAPIView(generics.ListAPIView):
    """Course All Available Listing.

    A student should be able to view the available courses.
    """
    queryset = Course.objects.filter(is_available=True)
    serializer_class = CourseSerializer


class EnrollCourse(generics.RetrieveUpdateAPIView):
    """Enroll a course.

    A student can enroll a course. A course can have limited students."""
    serializer_class = CourseSerializer

    def get_queryset(self):
        course = Course.objects.filter(pk=self.kwargs['pk'])
        return course

    def get(self, request, *args, **kwargs):
        course = self.get_queryset().values(
            'course_name').annotate(Count('user'))

        # allow only 5 users per course
        if course.first()['user__count'] < MAX_STUDENTS:
            request.user.course.add(self.get_object())
            request.user.save()
        else:
            return Response({"Error": "Course is full"},
                            status=status.HTTP_403_FORBIDDEN)

        if course.first()['user__count'] == MAX_STUDENTS:
            self.get_queryset().update(is_available=False)

        return Response({"Success": "Successfully enrolled"},
                        status=status.HTTP_201_CREATED)


class WithdrawCourse(generics.RetrieveUpdateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        course = Course.objects.filter(pk=self.kwargs['pk'])
        return course

    def get(self, request, *args, **kwargs):
        request.user.course.remove(self.get_object())
        request.user.save()

        course = self.get_queryset().values(
            'course_name').annotate(Count('user'))

        # update the is_available field when there are less than max students
        if course.first()['user__count'] < MAX_STUDENTS:
            self.get_queryset().update(is_available=True)

        return Response({"Success": "Successfully withdrawn from course"},
                        status=status.HTTP_201_CREATED)


