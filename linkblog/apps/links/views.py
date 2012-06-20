from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Content, Tag
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def unified_list(request):
    content_list = Content.objects.all()
    paginator = Paginator(content_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return render_to_response('links/content_list.html', {"items": items}, context_instance = RequestContext(request))

def tag_list(request, slug):
    tag = Tag.objects.get(slug=slug)
    tag_list = tag.content_set.all()
    
    paginator = Paginator(tag_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
         items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return render_to_response('links/tag.html', {"tag": tag, "items": items}, context_instance = RequestContext(request))

def detail(request, year, month, day, slug):
    item = Content.objects.get(created__year=year, created__month=month, created__day=day, slug=slug).as_leaf_class()
    return render_to_response(item.template, { 'item': item }, context_instance = RequestContext(request))
