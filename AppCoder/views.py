from django.shortcuts import render , redirect , HttpResponse

from .models import Curso
from .forms import CursoFormulario

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

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