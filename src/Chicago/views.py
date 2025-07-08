from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Cliente
from .forms import ClienteForm
import re

#HOME FUNCTIONS

def index(request):
    return render(request, 'Chicago/index.html')

#ABOUT ME FUNCTIONS

def about(request):
    return render(request, 'Chicago/about.html')

#STORE FUNCTIONS:

def store(request):
    return render(request, 'Store/index_store.html')
    
#SOCIAL MEDIA FUNCTIONS:

def socialmedia (request):
    return render(request, 'Chicago/socialmedia.html')

#REGISTER FUNCTIONS

def login_view(request):
    return render(request, 'Chicago/login.html')

def logout_view (request):
    logout(request)
    return redirect ("/")

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            
            password = form.cleaned_data.get('password1')
            
            if not re.search(r'[A-Z]', password):
                messages.error(request, 'La contraseña debe contener al menos una letra mayúscula.')
                return render(request, 'registro.html', {'form': form})

            if not re.search(r'[0-9]', password):
                messages.error(request, 'La contraseña debe contener al menos un número.')
                return render(request, 'registro.html', {'form': form})

            if len(re.findall(r'[a-zA-Z]', password)) < 3:
                messages.error(request, 'La contraseña debe tener al menos tres letras.')
                return render(request, 'registro.html', {'form': form})

            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('index')

        else:
            messages.error(request, 'Por favor corregí los errores en el formulario.')
    else:
        form = ClienteForm()

    return render(request, 'Chicago/login.html', {'form': form})


