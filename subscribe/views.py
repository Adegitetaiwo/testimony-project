from django.shortcuts import render
from .models import subscribeModel
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import subscribeForms

# Create your views here.


def subscribeView(request):
 
    
    return render(request, 'index.html', content)
