from django import forms


class SignUp(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    senha = forms.CharField(widget=forms.PasswordInput,label='Senha')