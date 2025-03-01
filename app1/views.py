from django.shortcuts import render

def hola_mundo (request):

    return render(request, 'hola_mundo.html') 

from django.views.generic import TemplateView

class Adios_Mundo(TemplateView):
    template_name = "adiosChao.html"
