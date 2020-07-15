from django.shortcuts import render

# Create your views here.


def trigger_error(request):
    division_by_zero = 1 / 0
