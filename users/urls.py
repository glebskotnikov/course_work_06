from users.views import LoginView, LogoutView, RegisterView, email_verification, PasswordResetView, ProfileView, \
    UserListView, toggle_activity
from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='users_list'),
    path('activity/<str:user_email>/', toggle_activity, name='toggle_activity'),
]
