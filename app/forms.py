from django.forms import ModelForm
from app.models import Productos


class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo', 'nombre', 'cantidad']
