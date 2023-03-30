from django import forms
from main_app.models import newTestimonies
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget


CHOICES = (
    ('salvation', 'Salvation'), 
    ('health', 'Health'),
    ('addiction', 'Addiction'),
    ('finance', 'Finance'),
    ('protection', 'Protection'),
     ('others', 'Others') 
     )

class createPostForms(forms.ModelForm):
    userId = forms.CharField(max_length=250, required=False)
    title = forms.CharField(max_length=260, required=True, widget=(forms.TextInput(attrs={'id':"fname", 'class':"form-control", 'placeholder':"Title : something to describe your Testimony"})))
    category = forms.ChoiceField(choices=CHOICES, required=False)
    #to be continue
    body = forms.CharField(widget=CKEditorWidget(attrs={'cols': '80', 'rows': '30'}))
    author =forms.CharField(max_length= 200, required=False)
    author_img = forms.ImageField(required=False)
    email = forms.CharField(max_length=300, required=False, widget=(forms.TextInput(attrs={'type':"email", 'id':"email", 'class':"form-control", 'placeholder':"an email to track your testimony status"})))
    class Meta:
        model = newTestimonies
        fields = '__all__'
 
