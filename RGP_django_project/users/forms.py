# customizabe form instad of using django default form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #default "field required" in place

	class Meta: # nested namespace for configurations to keep it in one place 
		model = User # model affected is "User", form.save will go to User
		fields = ['username', 'email', 'password1', 'password2'] #fields we want, and in what order