from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from .models import Libros

def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'inicio.html'

    def post():

        return

    def get(self, request):
        # ESta es mi clase GET #
        print('yainicio mi GET')

        return render(request, self.template_name)

def insertar_libro(request):
    nuevo_libro = Libros(
        titulo='El gran libro',
        edicion='Primera edicion',
        editorial='Editorial XYZ',
        año_pub=2022,
        pagina=200
    )
    nuevo_libro.save()

    return HttpResponse('Libro insertado correctamente')
