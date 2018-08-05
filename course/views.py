from django.shortcuts import render
from rest_framework import generics

from course.models import Course
from course.serializers import CourseSerializer


class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer