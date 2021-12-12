from django.urls import path
from django_app.apps.api.views import search

urlpatterns = [
    path('', search.SearchsView.as_view()),
]
