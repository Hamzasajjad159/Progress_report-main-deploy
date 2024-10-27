from django import template

register = template.Library()

@register.filter
def get_items(dictionary, key):
    """Get an item from a dictionary or list."""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    elif isinstance(dictionary, list) and isinstance(key, int):
        return dictionary[key]
    return None

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

