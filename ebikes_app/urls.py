from django.urls import path
from ebikes_app.views import form_add_bicicleta, form_search_bicicleta, form_add_insumo, form_add_usuario, home

urlpatterns = [
    path('home/',home),
    path('form_add_usuario/', form_add_usuario),
    path('form_add_bicicleta/', form_add_bicicleta),
    path('form_add_insumo/', form_add_insumo),
    path('form_search_bicicleta/', form_search_bicicleta),
]