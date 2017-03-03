from django import forms
from aplicativo.models import Uf
from django.forms import ModelForm

class FormUf(ModelForm):
	class Meta:
		model = Uf
		fields=('__all__')