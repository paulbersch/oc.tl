from django import template
from links.models import Content

register = template.Library()

@register.assignment_tag
def recent_content(count):
    return Content.objects.all()[:count]
