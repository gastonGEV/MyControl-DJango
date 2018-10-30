from django.shortcuts import render
from django.utils import timezone
from .models import Incidencia
from django.db.models import Sum

# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'myControl/post_list.html', {'posts': posts})

def incidencia_list(request):
    incidencias = Incidencia.objects.all()
    ingresos = Incidencia.objects.filter(tipo=1).aggregate(Sum('mount'))
    gastos = Incidencia.objects.filter(tipo=2).aggregate(Sum('mount'))
    return render(request, 'myControl/incidencias.html', {'incidencias': incidencias, 'ingresos':ingresos, 'gastos':gastos})

def incidencia(request, id):
    incidencia = Incidencia.objects.get(pk=id)
    return render(request, 'myControl/show.html', {'incidencia': incidencia})

def calendar(request, id):
    incidencias = Incidencia.objects.filter(created_date__month=id)
    return render(request, 'myControl/calendar.html', {'incidencias':incidencias})