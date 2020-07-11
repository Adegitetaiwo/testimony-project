from django.contrib import admin
from .models import publicUser, totalRegisteredUser
# Register your models here.
admin.site.register(publicUser)
admin.site.register(totalRegisteredUser)
