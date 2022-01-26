from django import template
from ..models import Menu


register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def menu(context):
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by("-priority").all()}

@register.inclusion_tag("menu.html", takes_context=True)
def profile(context):
    if context.request.user.is_authenticated:
        menu = [{
            'url': "about",
            'title': context.request.user.username,
        }]
        return {'menu': menu}

@register.inclusion_tag("menu.html", takes_context=True)
def login_menu(context):
    if context.request.user.is_authenticated:
        menu = [
        {
            'url': "logout",
            'title': "Выйти",
        }]
        return {'menu': menu}
    else:
        menu = [{
            'url': "reg",
            'title': 'Регистрация /',
        },
            {
                'url': "auth",
                'title':"Войти",
            }
        ]
    return {'menu': menu}



@register.inclusion_tag("menu.html", takes_context=True)
def about(context):
    if context.request.user.is_authenticated:
        menu = [{
            'url': "index_about",
            'title': "Ваши публикации",
        }]
        return {'about': menu}
    else:
        menu = [{
            'url': "account",
            'title': 'Ваши публикации ',
        }]
        return {'about': menu}

@register.inclusion_tag("menu.html", takes_context=True)
def post(context):
    if context.request.user.is_authenticated:
        menu = [{
            'url': "post",
            'title': 'Загрузка поста',
        }]
        return {'post': menu}