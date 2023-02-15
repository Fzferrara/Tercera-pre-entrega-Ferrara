from django.shortcuts import render , redirect 
from django.http import HttpResponse

from .models import Curso, Vendedor 
from .forms import CursoFormulario, VendedorFormulario

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def productos(request):
    return render(request, 'AppCoder/productos.html')

def vendedores(request):
    return render(request, 'AppCoder/vendedores.html')

def distribuidores(request):
    return render(request, 'AppCoder/distribuidores.html')

def entregas(request):
    return render(request, 'AppCoder/entregas.html')

def curso_formulario(request):
    
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso =  Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return redirect('inicio')
    
    
    else:
        mi_formulario = CursoFormulario()
    
    return render(request, 'AppCoder/curso-formulario.html', {'formulario_curso': mi_formulario, 'saludo': 'Por Favor, Registrese.'})


def busqueda_camada(request):
    return render(request, 'AppCoder/busqueda-camada.html')

def buscar(request):
    
    if request.GET['camada']:
        mi_camada = request.GET['camada']
        resultado = Curso.objects.filter(camada__icontains = mi_camada)

        return render(request, 'AppCoder/resultados-camada.html', {'cursos': resultado, 'camada': mi_camada})

    respuesta = 'No se encontro la camada solicitada'
    return HttpResponse(respuesta)


# def vendedorformulario(request):
#     if request.method == 'POST':
#         mi_formulario = VendedorFormulario(request.POST)
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             vendedor = Profesor(nombre=informacion['nombre'],
#                                 apellido=informacion['apellido'],
#                                 email=informacion['email'],
#                                 profesion=informacion['entrega'])
#             vendedor.save()
#             return redirect('inicio')
#     else:
#         mi_formulario = VendedorFormulario()
        
#     return render(request, 'AppCoder/vendedor-formulario.html', {'formulariovendedor': mi_formulario})

def vendedor_formulario(request):
    if request.method == 'POST':
        mi_formulario = VendedorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Vendedor(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                lugar=informacion['lugar'])
            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = VendedorFormulario()
        return render(request, 'AppCoder/vendedor-formulario.html', {'formulario_vendedor': mi_formulario})