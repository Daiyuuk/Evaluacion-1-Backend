from django.contrib import admin
from django.urls import path

# Importar vistas de ambas aplicaciones
import app1.views as views_app1
import app2.views as views_app2

import perfil.views as views_perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para App 1
    path('vista1/', views_app1.vista1_app1, name='vista1_app1'),
    path('vista2/', views_app1.vista2_app1, name='vista2_app1'),
    
    # Rutas para App 2
    path('vista1_app2/', views_app2.vista1_app2, name='vista1_app2'),
    path('vista2_app2/', views_app2.vista2_app2, name='vista2_app2'),

    # Ruta para la vista de perfil
    path('perfil/', views_perfil.perfil_uno, name='perfil_uno'),
    path('perfil2/', views_perfil.perfil_dos, name='perfil_dos')

]
