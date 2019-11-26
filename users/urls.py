from django.urls import path, include

from users import views

app_name = 'account'
urlpatterns = [
    path('register', views.register, name='register'),
]
