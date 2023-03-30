from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("detailed/<int:id>/<slug:slug>/",
         views.detailedPage, name='detailed'),
    #search engine path
    path('search', views.search, name='search'),
    path('salvation-category/', views.salvation, name='salvation'),
    path('health-category/', views.health, name='health'),
    path('addiction-category/', views.addiction, name='addiction'),
    path('finance-category/', views.finance, name='finance'),
    path('protection-category/', views.protection, name='protection'),
    path('others-category/', views.others, name='others'),
]
