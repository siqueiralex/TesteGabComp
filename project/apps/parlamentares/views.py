import httpx
import json
from django.views.generic import View
from django.shortcuts import render


class BuscaView(View):
    template_name = "parlamentares/busca.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        if 'nome' in request.GET:
            nome = request.GET.get('nome')
            r = httpx.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados?nome={nome}&ordem=ASC&ordenarPor=nome")
            response = r.json()
            context['parlamentares'] = response['dados']
        
        return render(request, self.template_name, context)