from django import forms
from .models import contactModel

class contactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, widget=(forms.TextInput(attrs={
        'id': 'fname',
        'class': 'form-control',
    })))
    last_name = forms.CharField(max_length=50, required=False, widget=(forms.TextInput(attrs={
        'id': 'lname',
        'class': 'form-control',
    })))
    email = forms.EmailField(required=False, widget=(forms.TextInput(attrs={
        'id': 'email',
        'type': 'email',
        'class': 'form-control',
    })))
    subject = forms.CharField(max_length=120, required=False, widget=(forms.TextInput(attrs={
        'id': 'subject',
        'type':'subject',
        'class': 'form-control',
    })))
    message = forms.CharField(required=False, widget=(forms.Textarea(attrs={
        'name':'message',
        'id':'message',
        'cols':30, 'rows': 7,
        'class': 'form-control',
        'placeholder': 'Write your notes or questions here...'
    })))

    class Meta:
        model = contactModel
        fields = '__all__'
