#--------------------------------------------------------------
'''importations necessaires pour utiliser forms.ModelForm qui 
permet de creer des forms a partir des tables crees dans models.py'''

from django import forms
'''on importe la table quon veut transformer en form'''
from app3.models import User
'''on importe django validators pour personnaliser nos
validations et lever des erreurs'''
from django.core import  validators


'''notre table qui recoit les informations de la form pour les mettre en
base de donnees'''
class RegisterUser(forms.ModelForm):

'''c'est le code pour transformer notre table en form'''
    class Meta():
        model=User
        fields ='__all__'

'''le code pour faire la verification des champs de donnees avant de les 
post'''

    """ def clean(self):
        
        #apparemment allCleanData est un dictionnaire
        allCleanData= super().clean()
        email=allCleanData['email']
        verifyEmail=allCleanData['verifyEmail']

        
        #si les deux champs saisis par l'utilisateur son differents
        #lever un message d'erreur et ne pas faire le post, 
        # dans le cas contraire le post se
        #fait avec success
        if email!=verifyEmail:
            raise forms.ValidationError("Emails doesn't match!") """