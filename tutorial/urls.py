from django.contrib import admin
from django.urls import (include, path)
from rest_framework import routers
from quickstart import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

schema_view = get_swagger_view(title='API Lists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickstart/', include(router.urls)),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view),
]
