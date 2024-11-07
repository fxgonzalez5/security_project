from django import forms
from .models import User


class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = User
        fields = ['name', 'username', 'password']  # Incluye otros campos que necesites

    def save(self, commit=True):
        # Guardar la contraseña encriptada
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
