from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key, sort = True):
    """
        Returns the value turned into a list.
    """
    list = value.split(key)
    if sort:
        list.sort()
    return list

@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)