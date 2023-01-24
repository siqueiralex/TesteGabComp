from django import template, forms
import re
from datetime import datetime, timedelta
from django.utils import timezone


register = template.Library()

@register.filter(name='is_floatable')
def is_floatable(field):
    return isinstance(field.field.widget, forms.widgets.TextInput)  \
        or isinstance(field.field.widget, forms.widgets.PasswordInput) \
        or isinstance(field.field.widget, forms.widgets.DateInput) \
        or isinstance(field.field.widget, forms.widgets.Select) \
        or isinstance(field.field.widget, forms.widgets.NumberInput)


@register.filter
def add_class(value, class_name):
    current_classes = value.field.widget.attrs.get('class', '')
    return value.as_widget(attrs={
        "class": " ".join((current_classes, class_name))
    })


@register.filter
def attrs(value, arg):
    no_spaces = arg.replace(' ', '')   
    args_list = no_spaces.split(',') 
    
    for arg_string in args_list:
        splitted = arg_string.split('=')
        value.field.widget.attrs[splitted[0]] = splitted[1]

    return value


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter
def dump_var(var):
    print(var)
    return var


@register.filter
def parse_bs_alert(var):
    mapping = {
        'error' : 'danger',
        'warning' : 'warning',
        'info' : 'success'
    }
    return mapping[var]


@register.filter
def replace(value, arg):
    """
    Replacing filter
    Use `{{ "aaa"|replace:"a|b" }}`
    """
    if len(arg.split('|')) != 2:
        return value

    what, to = arg.split('|')
    return str(value).replace(what, to)


@register.filter
def dictitem(dictionary, key):
    return dictionary.get(key)


@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None



@register.filter
def get_referer(request):
   return request.META.get('HTTP_REFERER')

@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)

@register.filter
def days_since(date):
    delta = timezone.now().date() - date
    return delta.days + 1



@register.filter
def plus_days(value, days):
    return value + timedelta(days=days)

@register.filter
def minus_days(value, days):
    return value - timedelta(days=days)