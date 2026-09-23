from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('perfil/', views.perfil_uno, name='perfil_uno'),
    path('perfil2/', views.perfil_dos, name='perfil_dos'),

    ]