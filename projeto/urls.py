"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from aplicativo.models import Uf
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from aplicativo import views

urlpatterns = [
	#Página inicial
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    #Admin
    url(r'^admin/', admin.site.urls),
    #CRUD UF
    url(r'^formUf/', views.FormUfView.as_view(template_name="form.html")),
    url(r'^listaUf/', views.UfListView.as_view(template_name="Uf/listaUf.html")),
    url(r'^editar/(?P<pk>[\w-]+)$', views.UfEdita.as_view(template_name="form.html")),
    url(r'^excluir/(?P<pk>[\w-]+)$', views.UfDelete.as_view()),
    #CRUD Municipio
    url(r'^formMunicipio$', views.MunicipioCreate.as_view(template_name="form.html")),
    url(r'^listaMunicipio', views.MunicipioListView.as_view(template_name="Municipio/listaMunicipio.html")),
    url(r'^editarMunicipio/(?P<pk>[\w-]+)$', views.MunicipioEdita.as_view(template_name="form.html")),
    url(r'^excluirMunicipio/(?P<pk>[\w-]+)$', views.MunicipioDelete.as_view()),
    #CRUD TipoGestao
    url(r'^formTipoGestao$', views.TipoGestaoCreate.as_view(template_name="form.html")),
    url(r'^listaTipoGestao', views.TipoGestaoListView.as_view(template_name="TipoGestao/listaTipoGestao.html")),
    url(r'^editarTipoGestao/(?P<pk>[\w-]+)$', views.TipoGestaoEdita.as_view(template_name="form.html")),
    url(r'^excluirTipoGestao/(?P<pk>[\w-]+)$', views.TipoGestaoDelete.as_view()),
    #CRUD Estabelecimento
    url(r'^formEstabelecimento$', views.EstabelecimentoCreate.as_view(template_name="form.html")),
    url(r'^listaEstabelecimento', views.EstabelecimentoListView.as_view(template_name="Estabelecimento/listaEstabelecimento.html")),
    url(r'^editarEstabelecimento/(?P<pk>[\w-]+)$', views.EstabelecimentoEdita.as_view(template_name="form.html")),
    url(r'^excluirEstabelecimento/(?P<pk>[\w-]+)$', views.EstabelecimentoDelete.as_view()),
    
]
