from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos
from .forms import ProductoForm

def index(request):

    return HttpResponse("Aqui se deberian mostar los productos")

class Vproductos(View):
    template_name = 'productos.html'

    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')

        return render(request, self.template_name, {'form': form})


    def get(self, request):
        form = ProductoForm()
        print('yainicio mi GET-----*')
        productos = Productos.objects.all()
        return render(request, self.template_name, {'form': form, 'productos': productos})

def insertar_producto(request):
    nuevo_producto = Productos(
        nombre='iPhone 14 Pro',
        descripcion='6.7" Negro espacial 128 GB',
        precio=25999.98,
        fec_reg='2022-09-15', #YYYY-MM-DD
        estatus=False
    )
    nuevo_producto.save()

    return HttpResponse('Producto insertado correctamente')