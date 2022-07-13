from django import forms

# Create your forms here.
class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class BicicletaForm(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    rodado = forms.IntegerField()
    precio = forms.DecimalField(max_digits=8,decimal_places=2)

class InsumoForm(forms.Form):
    marca = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.DecimalField(max_digits=8,decimal_places=2)

class BicicletaBusqueda(forms.Form):
    criterio = forms.CharField()