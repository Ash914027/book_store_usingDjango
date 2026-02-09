from django import forms
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm, UserCreationForm
from .models import User

class AuthenticationForm(DjangoAuthenticationForm):
    username = forms.CharField(max_length=20, required=False)
    # password = forms.CharField(widget=forms.Textarea, required=False)

    # You can override clean() or other methods if you want to use these fields for authentication or display

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=False)
    password = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
