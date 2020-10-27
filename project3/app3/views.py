from django.shortcuts import render
from django.http import HttpResponse
from app3.models import AccessRecord,User
from app3.forms import RegisterUser


# Create your views here.

'''les fonctions qui manipules la logique derriere les pages html
 de notre application'''

#------------------------------------------------------------------------
'''fonction qui permet d'afficher la homepage.html et sa logique'''
def homepage(request):
    return render(request, "html_stuff/homepage.html")



#------------------------------------------------------------------------

'''fonction qui permet d'afficher la homepage.html et sa logique'''

def helppage(request):
    
     '''newAccessRecord est un objet de tabe AccessRecord,
     on recupere les donnees de la table AccessRecord
     et on stoke dans newAccessRecord en les rangeant par la
     colonne date
     '''
    newAccessRecord = AccessRecord.objects.all().order_by('date')

    """on range la newAccessRecord dans un dictionnaire qui sera 
    #une parametre de la fonction render() """
    date_dict = {"newAccessRecordKey":newAccessRecord}
    return render(request, 'html_stuff/helppage.html', context=date_dict)


#---------------------------------------------------------------------------
'''fonction qui permet d'afficher la userpage.html et sa logique'''
def userpage(request):

   """ newUser est un objet de la table User,
   on recupere les donnees de la table User rangees par la colonne
    firstName et on stocke dans newUser"""
    newUser=User.objects.all().order_by('firstName')
    user_dict={"newUserKey" :newUser}
    return render(request,'html_stuff/userpage.html',context= user_dict)

#---------------------------------------------------------------------------
'''fonction qui permet d'afficher la signuppage.html et sa logique'''
def signuppage(request):

""" newRegisterUser est un objet de la form-table RegisterUser()
qui permet de stocker les donnees entrees par l'utilisateur
et les mettre dans la table User"""
    newRegisterUser=RegisterUser()

    """ Si l'utilisateur hits submit, recuperer ses donnees dans l'objet
    newRegisterUser"""
    if request.method=='POST':
        newRegisterUser=RegisterUser(request.POST)

        """ si c'est valide, mettre dans la table User et retourner a
        la homepage """
        if newRegisterUser.is_valid():
            newRegisterUser.save(commit=True)
            return homepage(request)
        else:
            print('invalid newRegisterUser')

    return render(request,'html_stuff/signup.html', {'newRegisterUserKey': newRegisterUser})