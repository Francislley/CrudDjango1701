from django.contrib import admin
from aplicativo.models import Uf, Estabelecimento, TipoGestao, Municipio
# Register your models here.
class UfAdmin(admin.ModelAdmin):
	list_display = ['sigla','nome']
	list_display_link = ['updated']
	list_filter = ['sigla']
	search_fields = ['sigla','nome']
	class Meta:
		model = Uf
class EstabelecimentoAdmin(admin.ModelAdmin):
	list_display = ['cnes','nome','razaoSocial']
	list_display_link = ['updated']
	list_filter = ['cnes']
	search_fields = ['cnes','nome','razaoSocial']
	class Meta:
		model = Estabelecimento
class TipoGestaoAdmin(admin.ModelAdmin):
	list_display = ['nome']
	list_display_link = ['updated']
	list_filter = ['nome']
	search_fields = ['nome']
	class Meta:
		model = TipoGestao
class MunicipioAdmin(admin.ModelAdmin):
	list_display = ['nome','uf']
	list_display_link = ['updated']
	list_filter = ['nome','uf']
	search_fields = ['nome','uf']
	class Meta:
		model = Municipio
admin.site.register(Uf, UfAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(TipoGestao, TipoGestaoAdmin)
admin.site.register(Municipio, MunicipioAdmin)