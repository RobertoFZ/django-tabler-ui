from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}), required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}), required=True)
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'rememberMe'}), required=False)
