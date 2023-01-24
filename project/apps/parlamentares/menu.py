from django.urls.base import reverse
from core.menu_lateral import ItemMenuLateral


def montar(request, items):
    items.append(ItemMenuLateral(titulo='Buscar Deputados', url = reverse("parlamentares:busca")))
    items.append(ItemMenuLateral(titulo='Deputados por Estado', url = reverse("parlamentares:estados")))