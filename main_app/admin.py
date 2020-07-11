from django.contrib import admin
from .models import newTestimonies, askedQuestion, bibleQuote

# Register your models here.
class newTestimoniesAdmin(admin.ModelAdmin):
    list_display = ['title', 'approved', 'created', 'updated']


admin.site.register(newTestimonies, newTestimoniesAdmin)
admin.site.register(askedQuestion)
admin.site.register(bibleQuote)
