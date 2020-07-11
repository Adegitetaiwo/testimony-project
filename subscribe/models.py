from django.db import models

# Create your models here.
class subscribeModel(models.Model):
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.email
    