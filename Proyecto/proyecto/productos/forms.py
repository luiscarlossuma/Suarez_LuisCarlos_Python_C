from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'fec_reg', 'estatus']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fec_reg = cleaned_data.get('fec_reg')
#        estatus = cleaned_data.get('estatus')

        if not nombre or not descripcion or not precio or not fec_reg :
            raise forms.ValidationError("Todos los campos deben estar completos")
        return cleaned_data