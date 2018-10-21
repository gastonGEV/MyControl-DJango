from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Incidencia


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myControl/post_list.html', {'posts': posts})

def incidencia_list(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'myControl/incidencias.html', {'incidencias': incidencias})

def incidencia(request, id):
    incidencia = Incidencia.objects.get(pk=id)
    return render(request, 'myControl/show.html', {'incidencia': incidencia} )
