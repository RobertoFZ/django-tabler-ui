from django.urls import path
from django.conf.urls import include
from django_app.apps.web.urls import dashboard, auth

urlpatterns = [
    # Auth urls
    path("auth/", include((auth, "auth"))),
    # Base URL's
    path("", include((dashboard, "dashboard"))),
]
