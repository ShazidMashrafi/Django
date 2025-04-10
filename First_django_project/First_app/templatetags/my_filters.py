from django import template

register = template.Library()

def my_filter(value):
    return value + " This is a string from custom filter"

def my_filter2(value,arg):
    return value + " " + arg

register.filter("custom_filter", my_filter)
register.filter("custom_filter2", my_filter2)