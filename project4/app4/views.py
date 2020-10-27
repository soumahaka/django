from django.shortcuts import render
from app4 import forms
# Create your views here.

def index(request):
    return render(request, "htmlfiles/index.html")


# La vue qui permet de manipuler notre form
def formPageView(request):
    #on cree un object de notre form
    mForm=forms.FormInfo()

    #si l'utilisateur appuis submit
    if request.method=='POST':
        mForm=forms.FormInfo(request.POST)
        #et ses donnees sont valide
        if mForm.is_valid():
            print("Valide Submission")
            print(mForm.cleaned_data['name'])
            print(mForm.cleaned_data['email'])
            print(mForm.cleaned_data['textarea'])

            #ses donnees sont stockees dans mForm mapee a une cle de dict
    return render(request,"htmlfiles/form.html", {"form":mForm})
