from django import template

register = template.Library()

def cutit(value, arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg,'')


register.filter("cutit", cutit)
