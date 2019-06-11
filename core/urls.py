from django.urls import path
from .views import home,cadastroUser


urlpatterns = [
    path('', home,name = 'home'),
    path('cadastro/',cadastroUser, name='url_cadastro_usuario'),

]
