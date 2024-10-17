from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('authapp.urls')),
    path('admin/', admin.site.urls),
]
