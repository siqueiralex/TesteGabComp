from django.urls import path

from . import views

app_name = 'parlamentares'

urlpatterns = [
        path('', views.BuscaView.as_view(), name='busca'),
]
