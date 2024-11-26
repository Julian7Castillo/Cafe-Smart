from django.shortcuts import render


# Create your views here.






def index(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'login.html')

def servicios(request):
    return render(request, 'servicios.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def inicio(request):
    return render(request, 'inicio.html')