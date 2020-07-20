from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import createPostForms, newTestimonies
from django.contrib.auth.decorators import login_required
from account.views import User
from django.contrib import messages
from account.models import publicUser

# Create your views here.

@login_required
def create_post(request):
    create_form = createPostForms(request.POST, request.FILES)
    if request.method == 'POST':
        if create_form.is_valid():
            create_form.instance.userId = '{}'.format(request.user.id)
            create_form.instance.email = '{}'.format(request.user.email)
            create_form.instance.author = '{} {}'.format(
                request.user.first_name, request.user.last_name)

            if create_form.instance.author_img:
                create_form.instance.author_img = request.user.publicuser.profile_img.url
            else:
                create_form.instance.author_img = ''

            #create_form.instance.author = '{} {}'.format(request.user.first_name, request.user.last_name)
            create_form.save()
            messages.success(
                request, 'Thank you so much for your submission, may your testimony remain permanent in Jesus name! please check the status of your testimony through your user profile and also share your testimony to your friends. If you have any problem with activating your testimony please contact us through the contact form')

            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'invalid request! Sorry somthing went wrong, Please make sure you are giving a valid email')
            return HttpResponseRedirect(request.path_info)
    else:

        content = {
            'create_new_testimony': create_form,
        }
        return render(request, 'create_post.html', content)
