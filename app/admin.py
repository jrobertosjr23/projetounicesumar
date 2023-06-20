from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UnidadeJudiciaria)
admin.site.register(models.Estado)
admin.site.register(models.Tribunal)

# admin.site.register(models.Nicho)
class NichoAdmin(admin.ModelAdmin):
    list_display = ("id", "unidade_judiciaria", "tribunal")
admin.site.register(models.Nicho, NichoAdmin)

admin.site.register(models.Cliente)
admin.site.register(models.Colaborador)
admin.site.register(models.Processo)