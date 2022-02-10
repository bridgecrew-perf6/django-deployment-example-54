from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,arg):
    """
    :param value:
    :param arg:
    :return: This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg, arg+' definitely')

# register.filter('cut', cut)