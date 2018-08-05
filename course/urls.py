from django.urls import path

from course.views import CourseAPIView, EnrollCourse, WithdrawCourse

urlpatterns = [
    path('all/', CourseAPIView.as_view(), name='all-course'),
    path('enroll/<int:pk>/', EnrollCourse.as_view(), name='enroll-course'),
    path('withdraw/<int:pk>/', WithdrawCourse.as_view(), name='withdraw-course'),
]