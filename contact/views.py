from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import contactForm
from subscribe.forms import subscribeForms
from main_app.models import askedQuestion
from django.core.mail import BadHeaderError, send_mail


# Create your views here.
def contact(request):
    contact_form = contactForm(request.POST or None)
    askedQuestions = askedQuestion.objects.all()


    if 'subject' in request.POST:
        if contact_form.is_valid:
            contact_form.save()
            messages.success(request, 'Thank You!, Your message has been recieved')
            send_mail('New Contact from Apostolictestimony', 'Hello Admin!, someone Contacted You throung the Contact form please check your dashboard', 
                    'apostolictestimony@gmail.com', ['adegitetaiwo24@gmail.com'], fail_silently=True)
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Invalid Form request')
            return HttpResponseRedirect(request.path_info)
    else:

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
            'contactForm': contact_form,
            'askedQuestions': askedQuestions,
            'form': subscribeForm,


        }
        return render(request, 'contact.html', content)
