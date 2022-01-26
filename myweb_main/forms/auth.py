from django import forms



class AuthForm(forms.Form):
        username = forms.CharField(label="Логин", max_length=128, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
        }))
        password = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
        }))


