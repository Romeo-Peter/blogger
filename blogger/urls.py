from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('account/', include('users.urls', namespace='account')),
    path('admin/', admin.site.urls),
]
