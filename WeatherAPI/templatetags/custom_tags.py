from django import template

register = template.Library()


@register.filter(name='index')
def get_list_item(list, index):
    try:
        return list[index]
    except IndexError:
        return None
