from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from Users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    path('adminpanal/', admin.site.urls),
    path("schema/generator/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("i18n/", include("django.conf.urls.i18n")),
    
    path("apis/", include(router.urls)),

]
