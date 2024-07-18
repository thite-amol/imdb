from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import (
    OR,
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    OperandHolder,
)
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from auth.permissions import IsOwner
from auth.serializers import (
    ChangePasswordSerializer,
    RegisterSerializer,
    UpdateUserSerializer,
)

from .serializers import RefreshTokenSerializer


@extend_schema(tags=["Auth"])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@extend_schema(tags=["Auth"])
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (OperandHolder(OR, IsOwner, IsAdminUser),)
    serializer_class = ChangePasswordSerializer


@extend_schema(tags=["Auth"])
class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (OperandHolder(OR, IsOwner, IsAdminUser),)


@extend_schema(tags=["Auth"])
class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RefreshTokenSerializer

    # def post(self, request):
    #     try:
    #         refresh_token = request.data["refresh_token"]
    #         token = RefreshToken(refresh_token)
    #         token.blacklist()
    #
    #         return Response(data=True, status=status.HTTP_205_RESET_CONTENT)
    #     except Exception as e:
    #         return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(data=True, status=status.HTTP_200_OK)


@extend_schema(tags=["Auth"])
class LogoutAllView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


@extend_schema(tags=["Auth"])
class DecoratedTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=["Auth"])
class DecoratedTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=["Auth"])
class DecoratedTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=["Auth"])
class DecoratedTokenBlacklistView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
