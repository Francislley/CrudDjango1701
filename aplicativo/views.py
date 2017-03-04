from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from aplicativo.forms import *
from aplicativo.models import Uf, Municipio, TipoGestao, Estabelecimento
from django.shortcuts import get_object_or_404
#CRUD UF
class FormUfView(FormView):
	template_name='form.html'
	form_class = FormUf
	success_url='/listaUf'
	
	def form_valid(self, form):
		form.save()
		return super(FormUfView, self).form_valid(form)

class UfListView(ListView):
	model = Uf
class UfEdita(UpdateView):
    model = Uf
    fields = ['nome']
    success_url = '/listaUf'
class UfDelete(DeleteView):
	model = Uf
	success_url = '/listaUf'
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

#CRUD MUNICIPIO
#Using create just for see whats happening
class MunicipioCreate(CreateView):
	model = Municipio
	fields = ['nome', 'uf']
	success_url = "/listaMunicipio"
class MunicipioListView(ListView):
	model = Municipio
class MunicipioEdita(UpdateView):
    model = Municipio
    fields = ['nome','uf']
    success_url = '/listaMunicipio'
class MunicipioDelete(DeleteView):
	model = Municipio
	success_url = '/listaMunicipio'
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

#CRUD TIPO GESTÃO
class TipoGestaoCreate(CreateView):
	model = TipoGestao
	fields = ['nome']
	success_url = "/listaTipoGestao"
class TipoGestaoListView(ListView):
	model = TipoGestao
class TipoGestaoEdita(UpdateView):
    model = TipoGestao
    fields = ['nome']
    success_url = '/listaTipoGestao'
class TipoGestaoDelete(DeleteView):
	model = TipoGestao
	success_url = '/listaTipoGestao'
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

#CRUD ESTABELECIMENTO
class EstabelecimentoCreate(CreateView):
	model = Estabelecimento
	fields = '__all__'
	success_url = "/listaEstabelecimento"
class EstabelecimentoListView(ListView):
	model = Estabelecimento
class EstabelecimentoEdita(UpdateView):
    model = Estabelecimento
    fields = ['nome','razaoSocial','municipio','tipoGestao','atendeSus']
    success_url = '/listaEstabelecimento'
class EstabelecimentoDelete(DeleteView):
	model = Estabelecimento
	success_url = '/listaEstabelecimento'
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)
