from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(CountryGDP)
class CountryGDPAdmin(ImportExportModelAdmin):
    list_display = ('name','year','code','value')
    list_filter = ['name']
    search_fields = ['name']