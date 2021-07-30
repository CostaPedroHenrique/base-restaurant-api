from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from menu import urls as menu_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(menu_urls)),
    path('api-auth/', include('rest_framework.urls')),
]
