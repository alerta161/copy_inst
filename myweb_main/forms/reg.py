from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from myweb_main.models import Profile


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.set_pasword(self.cleaned_data["password1"])
            if commit:
               user.save()
            return user