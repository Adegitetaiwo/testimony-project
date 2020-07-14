from django.shortcuts import render
from main_app.models import askedQuestion
from subscribe.forms import subscribeForms
from django.http import HttpResponseRedirect

# Create your views here.
def about(request):
    askedQuestions = askedQuestion.objects.all()

    subscribeForm = subscribeForms(request.POST or None)
    if 'email' in request.POST:
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)

    content = {
        'form': subscribeForm,
        'askedQuestions': askedQuestions
    }
    return render(request, 'about.html', content)
