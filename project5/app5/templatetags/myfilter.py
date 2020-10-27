""" Peut etre je vais commenter apres """

from django import template
register= template.Library()

@register.filter(name="cutting")
def cutting(value, oldvalue):

    return value.replace(oldvalue, 'newvalue')


#register.filter('cut', cut)