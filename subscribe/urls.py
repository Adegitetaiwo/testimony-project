from django.urls import path
from .views import *

urlpatterns = [
    path('subscribe', subscribeView, name='subscribe')
]
