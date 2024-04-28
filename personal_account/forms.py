from django import forms
from django.contrib.auth.forms import UserCreationForm
from personal_account.models import  User




class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Логин','class': 'form-input'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль','class': 'form-input'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля','class': 'form-input'}))
    experience = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Опыт', 'class': 'form-input'}))
    age = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Возраст', 'class': 'form-input'}))
    contact_information = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Контактная информация', 'class': 'form-input'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'experience', 'age', 'contact_information']


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CommentForm(forms.Form):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Вопрос', widget=forms.PasswordInput(attrs={'class': 'form-input'}))