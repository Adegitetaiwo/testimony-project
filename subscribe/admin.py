from django.contrib import admin
from .models import subscribeModel
# Register your models here.

class subscribeAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']


admin.site.register(subscribeModel, subscribeAdmin)
