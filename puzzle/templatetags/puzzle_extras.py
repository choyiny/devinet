from django import template
register = template.Library()

@register.filter
def userHasLevel(value, arg):
	return len(value.level_set.filter(id=arg)) > 0