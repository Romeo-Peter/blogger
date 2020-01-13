from django.urls import path, reverse_lazy

from users import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),

    path('login', auth_views.LoginView.as_view(
        template_name='users/accounts/login.html'), 
        name='login'),

    path('logout', auth_views.LogoutView.as_view(
        template_name='users/accounts/logout.html'), 
        name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/accounts/password_reset.html',
        success_url=reverse_lazy('account:password_reset_done')
        ),
        name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/accounts/password_reset_done.html'), 
    	name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(
        template_name='users/accounts/password_reset.html',
        success_url=reverse_lazy('account:password_reset_complete')
        ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetView.as_view(
        template_name='users/accounts/password_reset.html'), 
    	name='password_reset_complete'),
]