from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .forms import createPostForms, newTestimonies
from django.contrib.auth.decorators import login_required
from account.views import User
from django.contrib import messages
from account.models import publicUser
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import  PermissionDenied, RequestAborted
from account.forms import updateProfile
from django.core.mail import BadHeaderError, send_mail
import requests

# Create your views here.

def whatsapp_notification(request_ob, first_name, fail_silently=False):
    try:
        url = f'https:api.callmebot.com/whatsapp.php?phone=+2347017194423&text=Hello+👋+Admin,+you+got+a+new+*Testimony Submission*+from+*{first_name}*,+Login+to+your+Dashboard+to+review+the+testimony.+📎+https://apostolictestimony.herokuapp.com/admin/main_app/newtestimonies/+.&apikey=238215'
        request_ob.get(url)
    except Exception as e:
        if fail_silently == False:
            raise e
        # RequestAborted("Something went wrong when tring to make the request. \n Error: {e}")
        else:e.
        send_mail('AN ERROR OCCURED !',f' error -> {e.message}',
                      'apostolictestimony@gmail.com', ['apostolictestimony@gmail.com'], fail_silently=True)


            pass

@login_required
def create_post(request):
    create_form = createPostForms(request.POST, request.FILES)
    update_profile = updateProfile(request.POST, request.FILES, instance=request.user.publicuser)
    if request.method == 'POST':
        if create_form.is_valid():
            if update_profile.is_valid():
                create_form.instance.userId = '{}'.format(request.user.id)
                create_form.instance.email = '{}'.format(request.user.email)
                create_form.instance.author = '{} {}'.format(
                    request.user.first_name, request.user.last_name)
                #save profile image
                update_profile.save()

                if request.user.publicuser.profile_img:
                    create_form.instance.author_img = request.user.publicuser.profile_img
                else:
                    create_form.instance.author_img = ''

                #create_form.instance.author = '{} {}'.format(request.user.first_name, request.user.last_name)
                create_form.save()
                messages.success(
                    request, 'Thank you so much for your submission, may your testimony remain permanent in Jesus name! please check the status of your testimony through your user profile and also share your testimony to your friends. If you have any problem with activating your testimony please contact us through the contact form')
                send_mail('New Testimony Submit from Apostolictestimony', 'Hello Admin!, someone has just submitted a testimony, please check your dashboard',
                          'apostolictestimony@gmail.com', ['apostolictestimony@gmail.com'], fail_silently=True)
                
                whatsapp_notification(requests, create_form.instance.author, fail_silently=True)
                return HttpResponseRedirect(request.path_info)
            else:
                messages.error(
                    request, 'invalid request! Sorry somthing went wrong, Please make sure your uploaded file was an image')
                return HttpResponseRedirect(request.path_info)
             
        else:
            messages.error(request, 'invalid request! Sorry somthing went wrong, Please make sure you have filed the required inputs')
            return HttpResponseRedirect(request.path_info)
    else:

        content = {
            'create_new_testimony': create_form,
            'update_profile': update_profile,
        }
        return render(request, 'create_post.html', content)



def delete_post(request, id, slug):
    instance = get_object_or_404(newTestimonies, id=id, slug=slug)
    if '{} {}'.format(request.user.first_name, request.user.last_name) == instance.author:
        instance.delete()
        # messages.success(request, 'Done')
        return HttpResponseRedirect('/dashboard')
    else:
        raise PermissionDenied
        return HttpResponseRedirect('/dashboard')
