from django import forms
from .models import publicUser

CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Other'),
)

class updateProfile(forms.ModelForm):
    username = forms.CharField(required=False, widget=(forms.TextInput(attrs={'type':'text'})))
    gender = forms.ChoiceField(choices=CHOICES, required=False)
    city = forms.CharField(required=False, widget=(
        forms.TextInput(attrs={'type': 'text'})))
    country = forms.CharField(required=False, widget=(
        forms.TextInput(attrs={'type': 'text'})))
    
    class Meta:
        model = publicUser
        fields = '__all__'
        exclude = ['user']
