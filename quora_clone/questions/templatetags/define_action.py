from django import template
# Create your views here.
register = template.Library()

@register.simple_tag
def define(val=None):
  return val