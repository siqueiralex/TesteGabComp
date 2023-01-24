from dataclasses import dataclass
from django.apps import apps

@dataclass
class ItemMenuLateral:
    titulo:str = ""
    url:str = ""
    icone:str = ""
    


def montar_menu_lateral(request):
    items = []
    
    for app in apps.app_configs.values():
        if hasattr(app.module, 'menu'):
            if hasattr(app.module.menu, 'montar'):
                func_montar_menu = app.module.menu.montar
                func_montar_menu(request, items)


    return items