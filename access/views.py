from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
import random
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .forms import *
from .models import *


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.status = True
            user.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'resgister.html', {'form': form})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.status:
                    # Genera un código de verificación de 6 dígitos
                    verification_code = f"{random.randint(100000, 999999)}"
                    user.verification_code = verification_code
                    user.code_generated_at = timezone.now()
                    user.save()

                    # Enviar el correo con el código de verificación
                    send_mail(
                        'Código de Verificación',
                        f'Tu código de verificación es {verification_code}',
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )

                    # Guarda el ID del usuario en la sesión y redirige a la página de verificación
                    request.session['user_id'] = user.id
                    return redirect('verification')
                else:
                    form.add_error(None, "El usuario ya tiene una sesión activa.")
            else:
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def verificacion(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        code = request.POST.get('code')
        # Valida el código y su tiempo de expiración (5 minutos, por ejemplo)
        if code == user.verification_code and timezone.now() - user.code_generated_at < timedelta(minutes=5):
            user.status = True
            user.verification_code = None  # Limpia el código de verificación
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'verification.html', {'error': "Código incorrecto o expirado"})

    return render(request, 'verification.html')


def cerrar_sesion(request):
    if request.user.is_authenticated:
        request.user.status = False
        request.user.save()
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def panel(request):
    users = User.objects.all().prefetch_related('roles')
    context = {
        'users': users,
    }
    return render(request, 'dashboard.html', context)
