from django import template
register=template.Library()
@register.filter(name="get_replay")
def get_replay(dict, key):
    return dict.get(key)