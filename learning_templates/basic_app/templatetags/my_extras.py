from django import template

register = template.Library()

@register.filter(name='cut') # This is another way to register other than below line 12, using decorator
# Create custom filter "cut" and register it
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
# register.filter('cut',cut)
