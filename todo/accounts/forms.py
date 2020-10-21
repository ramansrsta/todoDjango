from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfileModel, Todo

class UserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']
        widgets = {
            'password' : forms.PasswordInput(attrs={
                'placeholder': 'Password from numbers and letters of the Latin alphabet'
            }),
            'username' : forms.TextInput(attrs={
                'placeholder' : 'Your Username'
            }),
            'first_name' : forms.TextInput(attrs={
                'placeholder' : 'First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'placeholder' : 'Last Name'
            })
        }

class UserProfileDetailsForm(ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['bio','dob']
        widgets = {
            'bio' : forms.TextInput(attrs={
                'placeholder': 'Say us about You!!'
            }),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150,widget=forms.PasswordInput())


class AddTodo(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']
        widgets = {
            'todo' : forms.TextInput(attrs={
                'placeholder' : 'Todo of Your'
            })
        }
