from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('incidencias', views.incidencia_list, name='incidencia_list'),
    path('incidencias/show/<int:id>', views.incidencia, name='incidencia'),
]
