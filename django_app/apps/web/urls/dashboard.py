from django.urls import path
from django_app.apps.web.views import dashboard as dashboard_views

urlpatterns = [
    path('', dashboard_views.IndexView.as_view(), name='index'),
]
