from django.shortcuts import render
from main_app.models import askedQuestion

# Create your views here.
def about(request):
    askedQuestions = askedQuestion.objects.all()

    content = {
        'askedQuestions': askedQuestions
    }
    return render(request, 'about.html', content)
