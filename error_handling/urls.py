from django.urls import path
from . import views
from .views import trigger_error

urlpatterns = [
    path('sentry-debug/', trigger_error),
]
