from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages

def barra(request):
    lista = Pages.objects.all()
    respuesta = "<ul>"
    for pagina in lista:
        respuesta += '<li><a href= "/pages/' + str(pagina.id) + '">' + pagina.name + "</a>"
    respuesta += "</ul>"
    return HttpResponse (respuesta)

@csrf_exempt
def pages (request, numero):
    if request.method == "POST":
        print (request.POST['name'], request.POST['page'])
        page = Pages(name = request.POST['name'], page = request.POST['page'])
        page.save()

    try:
        page = Pages.objects.get(id=str(numero))
    except Pages.DoesNotExist:
        return HttpResponseNotFound('<h1>' + numero + ' not found</h1>')
    return HttpResponse(page.name + " " + str(page.page))
