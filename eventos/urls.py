from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('registrar/', views.registrar_evento, name='registrar_evento'),
    path('detalle/<int:id>/', views.detalle_evento, name='detalle_evento'),
    path('eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:id>/', views.editar_evento, name='editar_evento'),
]