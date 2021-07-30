from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from menu import urls as menu_urls

schema_view = get_schema_view(
   openapi.Info(
      title="Base para cardápios",
      default_version='v1',
      description="Documentação da api base para cardápios",
      contact=openapi.Contact(email="devpedrohenrique@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('api/', include(menu_urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
