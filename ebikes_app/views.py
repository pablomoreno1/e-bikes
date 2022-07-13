from django.shortcuts import render

from ebikes_app.forms import BicicletaBusqueda, BicicletaForm, InsumoForm, UsuarioForm
from ebikes_app.models import Bicicleta, Insumo, Usuario

# Create your views here.

def home(request):
     return render(request,"ebikes_app/home.html",{})


def form_add_usuario(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid() :
            datos = formulario.cleaned_data
            usuario = Usuario(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                email=datos["email"]
                )
            usuario.save()
            formulario = UsuarioForm()
            return render(request,"ebikes_app/form_add_usuario.html",{"formulario":formulario,"mensaje":"Agregado con exito!!!"})
    else:
        formulario = UsuarioForm()

    return render(request,"ebikes_app/form_add_usuario.html",{"formulario":formulario})


def form_add_bicicleta(request):
    if request.method == "POST":
        formulario = BicicletaForm(request.POST)

        if formulario.is_valid() :
            datos = formulario.cleaned_data
            bicicleta = Bicicleta(
                marca=datos["marca"],
                modelo=datos["modelo"],
                rodado=datos["rodado"],
                precio=datos["precio"]
                )
            bicicleta.save()
            formulario = BicicletaForm()
            return render(request,"ebikes_app/form_add_bicicleta.html",{"formulario":formulario,"mensaje":"Agregado con exito!!!"})
    else:
        formulario = BicicletaForm()

    return render(request,"ebikes_app/form_add_bicicleta.html",{"formulario":formulario})


def form_add_insumo(request):
    if request.method == "POST":
        formulario = InsumoForm(request.POST)

        if formulario.is_valid() :
            datos = formulario.cleaned_data
            insumo = Insumo(
                marca=datos["marca"],
                descripcion=datos["descripcion"],
                precio=datos["precio"]
                )
            insumo.save()
            formulario = InsumoForm()
            return render(request,"ebikes_app/form_add_insumo.html",{"formulario":formulario,"mensaje":"Agregado con exito!!!"})
    else:
        formulario = InsumoForm()

    return render(request,"ebikes_app/form_add_insumo.html",{"formulario":formulario})

def form_search_bicicleta(request):
    busqueda = BicicletaBusqueda()

    buscado = False

    if request.GET:
        busqueda = BicicletaBusqueda(request.GET)
        if busqueda.is_valid():
            bicicletas = Bicicleta.objects.filter(marca=busqueda.cleaned_data.get("criterio")).all()
            return render(request, "ebikes_app/form_search_bicicleta.html", {"busqueda": busqueda, "bicicletas": bicicletas, "buscado": True})
            
    return render(request, "ebikes_app/form_search_bicicleta.html", {"busqueda": busqueda, "buscado": buscado})