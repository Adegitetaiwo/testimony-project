from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import publicUser
from .forms import updateProfile
from main_app.models import newTestimonies


# Create your views here.

#sign up view
def signUp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        comfirm_pass = request.POST['comfirm_pass']

        #check if email exist in database
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exist please Login')
            return HttpResponseRedirect(request.path_info)
        else:
            user = User.objects.create_user(username=email, first_name=first_name, last_name = last_name, email=email, password=password)
            user.save()
            publicUser.objects.create(
                user=user
            )
            messages.success(request, 'Your account has been created! Please Login to continue')
            return HttpResponseRedirect('/accounts/login')

    else:
        return render(request, 'sign_up.html')

#Login view
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Logined in')
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'login.html')
    
#Log Out view function
def logout(request):

    auth.logout(request)
    return HttpResponseRedirect('/')

#User profile view function
@login_required
def userProfile(request):
    userId = request.user.id  # get the unique email of the authenticated logined in user
    
    allPost = newTestimonies.objects.filter(userId=userId)
    approvedPost = newTestimonies.objects.filter(userId=userId,
        approved=True)
    pendingPost = newTestimonies.objects.filter(userId=userId,
        approved=False)

    context = {
        'Testimonies': allPost,
        'approved_testimony': approvedPost,
        'pending_testimomy': pendingPost,
    }
    return render(request, 'dashboard.html', context)

@login_required
def userProfileEdit(request):
    publicuser = request.user.publicuser
    forms = updateProfile(instance=publicuser)

    if request.method == 'POST':
        forms = updateProfile(request.POST, request.FILES, instance=publicuser)
        if forms.is_valid:
            forms.save()
    
    content = {
        'forms': forms,
    }
    return render(request, 'profile_edit.html', content)
