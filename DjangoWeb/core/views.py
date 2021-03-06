from core.forms import UserForm
from django.shortcuts import render

# Create your views here.

def form_user(request):
    datos = {
        'form':UserForm()
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request, 'registro.html', datos)

def home(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')
  
def inicio(request):
    return render(request,'login.html')

def galeria(request):
    return render(request,'galeria.html')

def contacto(request):
    return render(request,'contacto.html')

def contacto_c(request):
    return render(request,'contacto-correcto.html')    

def c_deportes(request):
    return render(request,'categoria-deportes.html')          

def c_ciencias(request):
    return render(request,'categoria-ciencias.html')

def c_actualidad(request):
    return render(request,'categoria-actualidad.html')

def c_politica(request):
    return render(request,'categoria-politica.html')    

def c_negocios(request):
    return render(request,'categoria-negocio.html')        

def n_noticias(request):
    return render(request,'nuevas-noticias.html')

def n_aceptada(request):
    return render(request,'noticia-aceptada.html')

def n_rechazada(request):
    return render(request,'noticia-rechazada.html')

def s_noticia(request):
    return render(request,'subir-noticia.html')        

def noticia_ciencias1(request):
    return render(request,'nuevo-mapa-estelar-1.html')

def noticia_ciencias2(request):
    return render(request,'agujero-negro-mas-cercano-tierra-2.html')

def noticia_ciencias3(request):
    return render(request,'contra-constelaciones-satelites-elon-musk-3.html')

def noticia_actualidad1(request):
    return render(request,'putin_amenazas.html')

def noticia_actualidad2(request):
    return render(request,'cerveza.html')

def noticia_actualidad3(request):
    return render(request,'funeral-masivo.html')

def noticia_deportes1(request):
    return render(request,'noticia_deporte.html')

def noticia_deportes2(request):
    return render(request,'noticia_deporte2.html')

def noticia_negocios1(request):
    return render(request,'banco.html')

def noticia_negocios2(request):
    return render(request,'mascarilla.html')

def noticia_negocios3(request):
    return render(request,'industria.html') 

def noticia_politica1(request):
    return render(request,'noticia_politica.html')

def noticia_politica2(request):
    return render(request,'noticia_politica2.html')                                
        