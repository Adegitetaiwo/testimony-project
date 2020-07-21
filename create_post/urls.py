from django.urls import path
from .views import *

urlpatterns = [
    path('new', create_post, name='create_post'),
    path('delete/<int:id>/<slug:slug>', delete_post, name='delete_post')

]
