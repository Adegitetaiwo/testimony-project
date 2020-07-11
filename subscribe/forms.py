from django import forms
from .models import subscribeModel

class subscribeForms(forms.ModelForm):
    email = forms.EmailField(required=False, widget=(forms.TextInput(attrs={
        'type':"email", 'id':'subscribe_input', 'name':"email", 'class':"form-control border-secondary text-white bg-transparent",
        'placeholder':"Enter Email" ,'aria-label':"Enter Email" ,'aria-describedby':"button-addon2"
    })))
    class Meta:
        model = subscribeModel
        fields = ('email', )
 
