from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.countries_gdp_list, name='countries_gdp_list'),
    path('countries_gdp_excel', views.countries_gdp_excel, name='countries_gdp_excel'),
    ]