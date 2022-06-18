from django import template

register = template.Library()


@register.filter()
def replace(value):
    value.replace("\033[1;34m", "")
    value.replace("\033[1;31m", "")
    value.replace("\033[1;32m", "")
    value.replace("\033[0m", "")
    return value


@register.filter()
def get_check_id(value):
    mylist = value.split(" ")
    return mylist[1]
