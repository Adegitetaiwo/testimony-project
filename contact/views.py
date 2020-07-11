from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import contactForm
from main_app.models import askedQuestion

# Create your views here.
def contact(request):
    contact_form = contactForm(request.POST or None)
    askedQuestions = askedQuestion.objects.all()


    if 'subject' in request.POST:
        if contact_form.is_valid:
            contact_form.save()
            messages.success(request, 'Thank You!, Your message has been recieved')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Invalid Form request')
            return HttpResponseRedirect(request.path_info)
    else:
        content = {
            'contactForm': contact_form,
            'askedQuestions': askedQuestions,

        }
        return render(request, 'contact.html', content)
