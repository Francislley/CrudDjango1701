from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from aplicativo.forms import *
from aplicativo.models import Uf, Municipio
from django.shortcuts import get_object_or_404
#CRUD UF
class FormUfView(FormView):
	template_name='Uf/formUf.html'
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
