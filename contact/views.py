from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import contactForm
from main_app.models import askedQuestion
from django.core.mail import BadHeaderError, send_mail


# Create your views here.
def contact(request):
    contact_form = contactForm(request.POST or None)
    askedQuestions = askedQuestion.objects.all()


    if 'subject' in request.POST:
        if contact_form.is_valid:
            email_subject = contact_form.instance.subject + \
                'from ' + contact_form.instance.email
            email_message = contact_form.instance.message
            contact_form.save()
            messages.success(request, 'Thank You!, Your message has been recieved')
            send_mail(email_subject, email_message, 'apostolictestimony@gmail.com', ['adegitetaiwo24@gmail.com'], fail_silently=True)
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
