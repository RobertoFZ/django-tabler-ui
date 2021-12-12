from django.urls import path
from django.conf.urls import include
from django_app.apps.api.urls import search

urlpatterns = [
    # Base URL's
    path("search/", include((search, "searchs"))),
]
