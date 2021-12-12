from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(name="replace_line_breaks", is_safe=True)
def replace_line_breaks(value):
    """
        Returns the value turned into a list.
    """
    return mark_safe(value.replace("\n", "<br/>"))


@register.filter(name="to_json", is_safe=True)
def to_json(value):
    """
        Returns the value turned into a list.
    """
    return mark_safe(json.dumps(value))
