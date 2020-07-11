from django.db import models

# Create your models here.

class contactModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return '{} from {} {}'.format(self.subject, self.first_name, self.last_name)
    
