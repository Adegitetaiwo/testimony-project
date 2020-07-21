from django.urls import path
import django.urls  as url
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('create-account/', signUp, name='signUp'),
    path('accounts/login/', login, name='login'),
    path('sign-out/', logout, name='sigout'),
    path('dashboard/', userProfile, name='dashboad'),
    path('dashboard/edit_profile', userProfileEdit, name='edit_profile'),
    #template_name='reset_password.html'
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='reset_password.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_form.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),

]
# path('dashboad/<slug:User.email>', login, name='dashboad')
