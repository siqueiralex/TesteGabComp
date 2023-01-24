from django.urls import path

from . import views

app_name = 'parlamentares'

urlpatterns = [
        path('', views.BuscaView.as_view(), name='busca'),
        path('parlamentar/<id>/', views.ParlamentarView.as_view(), name='detail'),
        path('estados/', views.EstadosView.as_view(), name='estados'),
        path('estados/<uf>/', views.EstadoView.as_view(), name='estado'),
]
