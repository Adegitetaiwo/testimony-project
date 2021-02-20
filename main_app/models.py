from django.db import models
from django.utils.text import slugify
from account.models import publicUser
from ckeditor.fields import RichTextField
# Create your models here.

Choise = (
    ('salvation', 'Salvation'),
    ('health', 'Health'),
    ('addiction', 'Addiction'),
    ('finance', 'Finance'),
    ('protection', 'Protection'),
    ('others', 'Others')



)
class newTestimonies(models.Model):
    userId = models.CharField(max_length=250, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="", editable=False)
    category = models.CharField(max_length=150, choices=Choise)
    body = RichTextField()
    author = models.CharField(max_length=50)
    author_img = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=254)
    approved = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    #save the slug to slugify(title)  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(newTestimonies, self).save(*args, **kwargs)


    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

    class Meta:
        verbose_name_plural = 'Testimonies'

class askedQuestion(models.Model):
    question = models.CharField(max_length=150)
    answer = RichTextField()

    def __str__(self):
        return '{}'.format(self.question)

    class Meta:
        verbose_name_plural = 'Set Frequency Asked Question'


class bibleQuote(models.Model):
    verse = models.CharField(max_length=150)
    quote = RichTextField()

    def __str__(self):
        return '{}'.format(self.verse)

    class Meta:
        verbose_name_plural = 'Bible Quote Header'
