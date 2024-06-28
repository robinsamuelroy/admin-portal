from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from admin_port import views



urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin interface
    path('', include('admin_port.urls')),  # Include app-specific URLs for admin_port
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
