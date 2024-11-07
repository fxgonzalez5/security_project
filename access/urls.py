from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registro, name='register'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('dashboard/', views.panel, name='dashboard'),
]
