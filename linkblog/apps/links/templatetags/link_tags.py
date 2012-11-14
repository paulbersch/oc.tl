from django import template
from links.models import Content, Tag

register = template.Library()

@register.assignment_tag
def recent_content(count):
    return Content.objects.all().order_by('updated')[:count]

@register.assignment_tag
def get_tags():
    return Tag.objects.all()
