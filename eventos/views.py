from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, RegistroEvento, Usuario
from .forms import EventoForm, RegistroEventoForm, UsuarioForm

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()

    return render(request, 'eventos/crear_evento.html', {
        'form': form
    })

def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = RegistroEventoForm()

    return render(request, 'eventos/registrar_evento.html', {'form': form})

def detalle_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    registros = RegistroEvento.objects.filter(evento=evento)

    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'registros': registros
    })

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('lista_eventos')

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/editar_evento.html', {'form': form})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'eventos/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'eventos/crear_usuario.html', {'form': form})