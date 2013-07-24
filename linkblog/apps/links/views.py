import sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Content, Link, Idea, Note, Tweet, Tag, Project, ReadingLog
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
# Create your views here.

categories = {
    's': Tweet,
    'l': Link,
    'i': Idea,
    'p': Project,
    'n': Note,
}

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

def category_list(request, category):
    content_list = categories[category].objects.all()
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

    return render_to_response('links/category_list.html', {"items": items}, context_instance = RequestContext(request))

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

def detail(request, type, year, month, day, slug):
    item = get_object_or_404(Content, created__year=year, created__month=month, created__day=day, slug=slug).as_leaf_class()
    return render_to_response(item.template, { 'item': item }, context_instance = RequestContext(request))

def book_detail(request, book, year, month, day, slug):
    item = get_object_or_404(ReadingLog, book__slug= book, created__year=year, created__month=month, created__day=day, slug=slug).as_leaf_class()
    return render_to_response(item.template, { 'item': item }, context_instance = RequestContext(request))
