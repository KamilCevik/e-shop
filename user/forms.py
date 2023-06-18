from django import forms
from django.forms.widgets import TextInput, EmailInput, Select, FileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Username")
    email = forms.EmailField(max_length=150, label="Email")
    first_name = forms.CharField(max_length=50, label="Name")
    last_name = forms.CharField(max_length=50, label="Surname")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }
