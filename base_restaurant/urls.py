from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers


from menu.api.viewsets import (PlateViewSet, GroupViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Base para cardápios",
      url='/api/',
      default_version='v1',
      description="Documentação da api base para cardápios",
      contact=openapi.Contact(email="devpedrohenrique@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

router = routers.DefaultRouter()
router.register(r'plates', PlateViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
