from django.urls import path
from .views import cadastro_estoque
from .views import lista_estoque


urlpatterns = [
    path('', lista_estoque,name = 'url_lista_estoque'),
    path('cadastro/',cadastro_estoque,name = 'url_cadastro_estoque')

]
