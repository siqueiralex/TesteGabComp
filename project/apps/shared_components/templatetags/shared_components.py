from django_component import Library, Component
from django.template.exceptions import TemplateSyntaxError

register = Library()

@register.component
class MenuLateral(Component):
    template = "shared_components/menu_lateral.html"
    
    def context(self, *args, **kwargs):
        from core.menu_lateral import montar_menu_lateral

        request = kwargs.get('request', None)
        return { **kwargs, 'menu' : montar_menu_lateral(request)}


@register.component
class ItemMenuLateral(Component):
    template = "shared_components/item_menu_lateral.html"
