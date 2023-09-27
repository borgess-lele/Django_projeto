from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from trufa.views import TrufaViewSet

router = DefaultRouter()
router.register(r"trufas", TrufaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]