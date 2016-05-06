from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from app.forms import ProductoForm
from app.models import Productos


class Home(View):
    form = ProductoForm()
    template_name = 'app/home.html'

    def get(self, request):
        context = {}
        context['form'] = self.form
        productos = Productos.objects.all()
        context['productos'] = productos
        return render(request, self.template_name, context)

    def post(self, request):
        if request.is_ajax():
            producto_id = request.POST.get('id')
            producto = get_object_or_404(Productos, pk=producto_id)
            producto.codigo = request.POST.get('codigo')
            producto.nombre = request.POST.get('nombre')
            producto.cantidad = request.POST.get('cantidad')
            producto.save()
            return HttpResponse("Success")

        form = ProductoForm(request.POST)
        context = {}

        if form.is_valid():
            form.save()

        productos = Productos.objects.all()
        context['form'] = form
        context['productos'] = productos
        return render(request, self.template_name, context)
