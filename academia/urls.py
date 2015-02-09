from django.conf.urls import patterns, include, url
from django.contrib import admin
from usuarios.views import *
from login.views import home, auth_view
from aparelhos.models import Aparelho
from aparelhos.views import listarAparelho




urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    
  #This is my first test with user login
    url('accounts/login/$','usuarios.views.login'),
    url('accounts/auth/$','usuarios.views.auth_view'),
    url('accounts/logout/$','usuarios.views.logout'),
    url('accounts/loggedin/$','usuarios.views.loggedin'),
    url('accounts/invalid/$','usuarios.views.invalid_login'),
    
    #Telas de Criacao para os models                                                     
    url('aparelho/create/$','aparelhos.views.create'),
    url('categoria/create/$','aparelhos.views.createCategoria'),
    url('exercicio/create/$','aparelhos.views.createExercicio'),
                    
    #Telas de Listagem
    url('aparelhos/$', listarAparelho.as_view(),name='detail'),
       
                       
)





