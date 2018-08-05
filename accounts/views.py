# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.permissions import IsAdminOrIsSelf
from .serializers import RegistrationSerializer, PasswordSerializer, \
    UserSerializer


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResetPasswordView(generics.RetrieveUpdateAPIView):
    """Set the users password.

    example of json input
    {
        "old_password": "password123",
        "new_password": "abcd1234"
    }
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrIsSelf,)

    def put(self, request, *args, **kwargs):
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object()

            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

