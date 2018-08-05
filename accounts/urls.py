from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import RegistrationAPIView, ResetPasswordView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls))
    path('register/', RegistrationAPIView.as_view()),
    path('reset-password/<int:pk>/', ResetPasswordView.as_view()),
]
