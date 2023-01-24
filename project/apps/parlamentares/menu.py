from django.urls.base import reverse
from core.menu_lateral import ItemMenuLateral


def montar(request, items):
    items.append(ItemMenuLateral(titulo='Buscar Parlamentares', url = reverse("parlamentares:busca")))