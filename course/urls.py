from django.urls import path

from course.views import CourseAPIView

urlpatterns = [
    path('all/', CourseAPIView.as_view())
]