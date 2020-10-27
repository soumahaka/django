from django import forms
from django.contrib.auth.models import User
from app6_1.models import ExtendedUser

""" Creation de la form qui va utiliser les champs de la 
table User de django """

class UserForm(forms.ModelForm):
    print(__name__ + " GOT CALLED" +"\n\n\n")
    """ Ce password, c'est lui qui est dans fields juste en bas
    il est different du champs password que User de django dispose"""
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model= User
        fields=('username', 'email', 'password')
class ExtendedUserForm(forms.ModelForm):
    class Meta():
        model = ExtendedUser
        fields=('WebSite', 'Picture')