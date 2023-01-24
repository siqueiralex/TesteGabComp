import httpx
import json
from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages


class BuscaView(View):
    template_name = "parlamentares/busca.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        if 'nome' in request.GET:
            nome = request.GET.get('nome')
            
            with httpx.Client() as client:
                try:
                    r = client.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados?nome={nome}&ordem=ASC&ordenarPor=nome", timeout=1)
                    response = r.json()
                    if response:
                        context['parlamentares'] = response['dados']
            
                except httpx.TimeoutException as e:
                    messages.error(self.request, f'OPS! Parece que a API de dados abertos está fora do ar... =/')
                    return render(request, self.template_name, context)
                except Exception as e:
                    return render(request, self.template_name, context)
                
        
        
        return render(request, self.template_name, context)


class ParlamentarView(View):
    template_name = "parlamentares/detail.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        id_deputado = kwargs.get('id', None)
        if id_deputado is not None:
            with httpx.Client() as client:
                try:
                    r = httpx.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}", timeout=1)
                    response = r.json()
                    if response:
                        context['dados_parlamentar'] = response['dados']
                    
                    r = httpx.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/ocupacoes", timeout=1)
                    response = r.json()
                    if response:
                        context['curriculo'] = response['dados']
            
                except httpx.TimeoutException as e:
                    messages.error(self.request, f'OPS! Parece que a API de dados abertos está fora do ar... =/')
                    return render(request, self.template_name, context)
                except Exception as e:
                    return render(request, self.template_name, context)
                
   
            
        return render(request, self.template_name, context)
    
class EstadosView(View):
    template_name = "parlamentares/estados.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        with httpx.Client() as client:
            try:
                r = httpx.get("https://dadosabertos.camara.leg.br/api/v2/referencias/deputados/siglaUF", timeout=1)
                response = r.json()
                if response:
                    context['UFs'] = response['dados']
            except httpx.TimeoutException as e:
                messages.error(self.request, f'OPS! Parece que a API de dados abertos está fora do ar... =/')
                return render(request, self.template_name, context)
            except Exception as e:
                return render(request, self.template_name, context)
            
   
            
        return render(request, self.template_name, context)

class EstadoView(View):
    template_name = "parlamentares/estado.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        uf = kwargs.get('uf', None)
        
        sigla_nome = {
            'ac' : 'Acre',
            'al' : 'Alagoas',
            'am' : 'Amazonas',
            'ap' : 'Amapá',
            'ba' : 'Bahia',
            'ce' : 'Ceará',
            'df' : 'Distrito Federal',
            'es' : 'Espírito Santo',
            'go' : 'Goiás',
            'ma' : 'Maranhão',
            'mg' : 'Minas Gerais',
            'ms' : 'Mato Grosso do Sul',
            'mt' : 'Mato Grosso',
            'pa' : 'Pará',
            'pb' : 'Paraíba',
            'pe' : 'Pernambuco',
            'pb' : 'Paraíba',
            'pi' : 'Piauí',
            'pr' : 'Paraná',
            'rj' : 'Rio de Janeiro',
            'rn' : 'Rio Grande do Norte',
            'ro' : 'Rondônia',
            'rr' : 'Roraima',
            'rs' : 'Rio Grande do Sul',
            'sc' : 'Santa Catarina',
            'se' : 'Sergipe',
            'sp' : 'São Paulo',
            'to' : 'Tocantins',
        }
        
        if uf is not None:
            with httpx.Client() as client:
                try:
                    r = client.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados?siglaUf={uf}&ordem=ASC&ordenarPor=nome", timeout=1)
                    response = r.json()
                    if response:
                        context['parlamentares'] = response['dados']
                    context['uf_nome'] = sigla_nome[uf.lower()]
                    
                except httpx.TimeoutException as e:
                    messages.error(self.request, f'OPS! Parece que a API de dados abertos está fora do ar... =/')
                    return render(request, self.template_name, context)
                except Exception as e:
                    return render(request, self.template_name, context)
            
   
            
        return render(request, self.template_name, context)