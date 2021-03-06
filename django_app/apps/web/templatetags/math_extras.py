from django import template

register = template.Library()


@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg

@register.filter(name='percentage')
def percentage(value, total):
    return (value * 100) / total