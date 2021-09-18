from django.views import View
from rest_framework.permissions import IsAuthenticated
# from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.shortcuts import redirect

from django.contrib.auth import get_user_model
User = get_user_model()


class Users(generics.ListAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        return queryset


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save(update_fields=['is_active'])
            # login(request, user)
            return redirect('/')
        else:
            # messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/')
