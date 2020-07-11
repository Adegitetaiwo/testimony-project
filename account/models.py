from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class publicUser(models.Model):
    user = models.OneToOneField(User, verbose_name="", null=True, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    username = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    def __str__(self):
        return '{}'.format(self.user)

class totalRegisteredUser(models.Model):
    CurrentNumber = models.PositiveIntegerField(verbose_name="Current Registered Number")
    def __str__(self):
        return self.CurrentNumber
    class Meta:
        verbose_name_plural = 'Total Registered User'
    
