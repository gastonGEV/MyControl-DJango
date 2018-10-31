from django.urls import path
from . import views


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.incidencia_list, name='incidencia_list'),
    path('<int:id>', views.incidencia_list, name='incidencia_list'),
    path('show/<int:id>', views.incidencia, name='incidencia'),
    path('calendar/<int:id>', views.calendar, name='calendar'),
]
