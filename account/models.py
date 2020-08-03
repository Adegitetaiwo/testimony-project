from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class publicUser(models.Model):
    user = models.OneToOneField(User, verbose_name="", null=True, on_delete=models.CASCADE)
    profile_img = CloudinaryField('image')
    username = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.user)

class totalRegisteredUser(models.Model):
    CurrentNumber = models.PositiveIntegerField(verbose_name="Current Registered Number")
    def __str__(self):
        return self.CurrentNumber
    class Meta:
        verbose_name_plural = 'Total Registered User'
    
