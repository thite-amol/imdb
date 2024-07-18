from django.urls import path

from auth.views import (
    ChangePasswordView,
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
    LogoutAllView,
    LogoutView,
    RegisterView,
    UpdateProfileView,
)

app_name = "auth"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path(
        "change_password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path(
        "profile/<int:pk>/",
        UpdateProfileView.as_view(),
        name="auth_update_profile",
    ),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
    path("logout_all/", LogoutAllView.as_view(), name="auth_logout_all"),
    path(
        "token/",
        DecoratedTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        DecoratedTokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
