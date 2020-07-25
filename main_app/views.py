from django.shortcuts import render, get_object_or_404
from .models import newTestimonies, askedQuestion, bibleQuote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from subscribe.forms import subscribeForms
from django.contrib import messages
from django.http import HttpResponseRedirect
import cloudinary
import cloudinary.uploader
import cloudinary.api
# from urllib import quote_plus
# Create your views here.


def page_pagination(page_request_varable, page, paginator):

    '''the value of the query will be past when the GET request is made to get a particular page with n post
        check to confirm the value been passed to the query'''

    try:
        #if the number of of the page passed exist - assing it to 'paginated_query'
        paginated_query = paginator.page(page)
    except PageNotAnInteger:  # if there was a PageNotAnInteger exception return the first page
        paginated_query = paginator.page(1)
    except EmptyPage:  # if there was a PageNotAnInteger exception return the last page
        paginated_query = paginator.page(paginator.num_pages)

    return paginated_query

def index(request):
    testimony = newTestimonies.objects.filter(approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()
    bible_quotes = bibleQuote.objects.last()

    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6 , allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''

    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)
    
    content = {
        'testimonies': recent_testimony,
        'form': subscribeForm,
        'askedQuestions': asked_questions,
        'bibleQuotes': bible_quotes,

        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable' : page_request_varable,
        'paginated_posts': paginated_query,
        'paginator':paginator,
    }

    return render(request, 'index.html', content)

#view for salvation section
def salvation(request):
    testimony = newTestimonies.objects.all().filter(
        category='salvation', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()

    
    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''

    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)

    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,

        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'salvation.html', content)

#view for health section


def health(request):
    testimony = newTestimonies.objects.all().filter(
        category='health', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()


    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''

    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)

    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,


        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'health.html', content)

#view for addiction section


def addiction(request):
    testimony = newTestimonies.objects.all().filter(
        category='addiction', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()

    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''
    
    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)


    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,


        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'addiction.html', content)

#view for finance section


def finance(request):
    testimony = newTestimonies.objects.all().filter(
        category='finance', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()

    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)
    
    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''
    
    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)

    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,


        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'finance.html', content)

#view for protection section


def protection(request):
    testimony = newTestimonies.objects.all().filter(
        category='protection', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()

    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''
    
    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)

    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,

        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,

        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'protection.html', content)

#view for others section


def others(request):
    testimony = newTestimonies.objects.all().filter(
        category='others', approved=True).order_by('-id')
    recent_testimony = newTestimonies.objects.filter(
        approved=True).order_by('-id')[:7]
    asked_questions = askedQuestion.objects.all()

    #category counts
    salvation_cat = newTestimonies.objects.filter(
        category='salvation', approved=True)
    health_cat = newTestimonies.objects.filter(
        category='health', approved=True)
    addiction_cat = newTestimonies.objects.filter(
        category='addiction', approved=True)
    finance_cat = newTestimonies.objects.filter(
        category='finance', approved=True)
    protection_cat = newTestimonies.objects.filter(
        category='protection', approved=True)
    others_cat = newTestimonies.objects.filter(
        category='others', approved=True)

    paginator = Paginator(testimony, 6, allow_empty_first_page=False)
    page_request_varable = 'p'
    page = request.GET.get(page_request_varable)

    try:
        paginated_query = page_pagination(page_request_varable, page, paginator)
    except EmptyPage:
        paginated_query = ''

    subscribeForm = subscribeForms(request.POST or None)
    if request.method == 'POST':
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)


    content = {
        'testimonies': recent_testimony,
        'askedQuestions': asked_questions,
        'form': subscribeForm,


        #category count
        'salvation_cat_count': salvation_cat.count,
        'health_cat_count': health_cat.count,
        'addiction_cat_count': addiction_cat.count,
        'finance_cat_count': finance_cat.count,
        'protection_cat_count': protection_cat.count,
        'others_cat_count': others_cat.count,
        
        'page_request_varable': page_request_varable,
        'paginated_posts': paginated_query,
        'paginator': paginator,
    }
    return render(request, 'others.html', content)


def detailedPage(request, id, slug):
    post = get_object_or_404(newTestimonies, id=id, slug=slug)
    all_testimony = newTestimonies.objects.filter(approved=True).order_by('-id')[:3]

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
        'Post':post,
        'all':all_testimony,
        'form': subscribeForm,

        'pageLink': request.build_absolute_uri(),
    }
    return render(request, 'detailed-single.html', content)

#search view
def search(request):
    post_list = newTestimonies.objects.filter(approved=True)
    query_search = request.POST['search']
    if query_search:
        post_list = post_list.filter(
            Q(title__icontains= query_search) |
            Q(category__icontains=query_search) |
            Q(body__icontains=query_search) 
        ).distinct()
    else:
        pass

    subscribeForm = subscribeForms(request.POST or None)
    if 'email' in request.POST:
        if subscribeForm.is_valid:
            subscribeForm.save()
            #messages.success(request, 'Thamks for your Subscription!')
            return HttpResponseRedirect(request.path_info)
        else:
            #messages.error(request, 'Invalid')
            return HttpResponseRedirect(request.path_info)


    content={
        'post_result': post_list,
        'form': subscribeForm,
        'keyword': query_search,
    }
    return render(request, 'search_result.html', content)
