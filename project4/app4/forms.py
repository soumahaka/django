from django import forms
from django.core import validators


#def checkFirstLetter(value):
#    if value[0].lower() !='z':
#        raise forms.ValidationError("Name need to start with z please !z")

#-----------------------------------------------------------------------------

#La class form de notre page de champs de saisie
class FormInfo(forms.Form):
    #name=forms.CharField(validators=[checkFirstLetter])

    #les champs de saisie donnees a l'utilisateur
    name=forms.CharField()
    email=forms.EmailField()
    #s'assurer que l'utilisateur n'est pas un robot mafieux
    verifyEmail=forms.EmailField(label="Enter your email again please!")
    textarea=forms.CharField(widget=forms.Textarea)

    #botdata=forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                            validators= [validators.MaxLengthValidator(0)])
    
    #la fonction de verification des champs de donnees quand l'utilisateur
    #clique sur submit avant de post
    def clean(self):
        #apparemment allCleanData est un dictionnaire
        allCleanData= super().clean()
        emailCleaning=allCleanData['email']
        verifyEmailCleaning=allCleanData['verifyEmail']
        
        #si les deux champs saisis par l'utilisateur son differents
        #lever un message d'erreur, dans le cas contraire le post se
        #fait avec success
        if emailCleaning!=verifyEmailCleaning:
            raise forms.ValidationError("Emails doesn't match!")