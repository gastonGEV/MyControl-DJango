from django.shortcuts import render
from django.utils import timezone
from .models import Incidencia
from django.db.models import Sum
from pprint import pprint
from django.core.paginator import Paginator

# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'myControl/post_list.html', {'posts': posts})

def incidencia_list(request, id=1):
    incidencia_list = Incidencia.objects.filter(created_date__month=id)
    ingresos = Incidencia.objects.filter(tipo=1, created_date__month=id).aggregate(Sum('mount'))
    gastos = Incidencia.objects.filter(tipo=2, created_date__month=id).aggregate(Sum('mount'))

    paginator = Paginator(incidencia_list, 5)  # Show 10 incidencias per page

    page = request.GET.get('page')
    incidencias = paginator.get_page(page)

    return render(request, 'myControl/incidencias.html', {'incidencias': incidencias, 'ingresos':ingresos, 'gastos':gastos})

def incidencia(request, id):
    incidencia = Incidencia.objects.get(pk=id)
    return render(request, 'myControl/show.html', {'incidencia': incidencia})

def calendar(request, id):
    mes = Incidencia.objects.filter(created_date__month=id)[:1]
    incidencias = Incidencia.objects.filter(created_date__month=id)
    
    return render(request, 'myControl/calendar.html', {'incidencias':incidencias, 'mes':mes})
