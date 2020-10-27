from django.shortcuts import render
from app6_1.forms import ExtendedUserForm, UserForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.

""" la homepage """
def homescenario(request):
    return render(request, "htmlfiles/homepage.html")


def registerscenario(request):
    print(" ENTERED REGISTERPAGE" +"\n\n\n")

    """ temoin embarque dans le dict de registerpage.html 
    qui nous permet soit dafficher la register form
    ou un msg de merci de vous enregistrer """
    registered=False
    
    if request.method!="POST":

        newUserForm=UserForm()
        newExtendedUserForm=ExtendedUserForm()
        
    else:
        print("USER HIT REGISTER !! "+"\n\n\n")

        """ quand le user hits submit, on recupere ses donnees """
        newUserForm= UserForm(data=request.POST)
        newExtendedUserForm=ExtendedUserForm(data=request.POST)

        """ on verifie si ses donnees sont valides """
        if newUserForm.is_valid() and newExtendedUserForm.is_valid():

            """ on save ses donnees sans les commit pour crypter son password avant
            de save dans la database """
            user=newUserForm.save(commit=False)
            """chercher et crypter le passwordfield dans user et le mettre dans password 
            de User de django """
            user.set_password(user.password)

            """ on save maintenant les champs de user"""
            user.save()

            """ on save les donnees des champs supplementaires sans les
            commit dans la database """
            extendedUser=newExtendedUserForm.save(commit=False)
            """ on fait la fusion de ces donnees maintenant pour obtenir les donnees
            dun seul utilisateur """
            extendedUser.linkedToUser=user
                        
            
            """ request.Files est un dictionnaire des imageField """
            if 'Picture' in request.FILES:
                extendedUser.Picture=request.FILES['Picture']
            
            """ on save les donnees supplement """
            extendedUser.save()

            """ le temoin signal que c'est valide cote html """
            registered=True

            """ si les donnees ne sont pas valides, lever des erreurs """    
        else:
            print(newUserForm.errors, newExtendedUserForm.errors)

    """ nous avons deux version de ce return, 
    version 1 : register=false et newUserForm et newExtendedUserForm sont vides
    puis on propose au user de s enrgistrer
    
    version 2 : register=true et newUserForm et newExtendedUserForm  contiennent les
    donnees du user quon a exploiter dans if request.method==post  """

    return render(request, "htmlfiles/registerpage.html", 
    {'registeredKey': registered, 'newUserFormKey':newUserForm, 'newExtendedUserFormKey':
    newExtendedUserForm})



#--------------------------------------------------------------------------------------------------------

""" la logique qui gere le hit du user sur login """
def loginscenario(request):

    if request.method=='POST':
        print("USER HIT LOGIN !! "+"\n\n\n")
        "re"
        username=request.POST.get("username")
        password=request.POST.get("password")

        "django gere la logique de connection avec la database"
        authenticatedUser=authenticate(username=username, password=password)

        """ si le user a ete authentifie avec success, """
        if authenticatedUser:
            print("USER HAS BEEN AUTHENTICATED")

            """ si le user est actif, """
            if authenticatedUser.is_active:
                """ le connecter! """
                login(request, authenticatedUser)
                """ puis le diriger vers la page appropriee, dans ce cas, homepage 
                dans urls.py """
                return HttpResponseRedirect(reverse('homepage'))

            #""" si user n'est pas actif """
            else: 
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            """ si user n'a pas ete authentifie avec succes, ses donnees ne
            se trouvent pas dans la base de donnees, lui afficher une page
            contenant un msg d'erreur """

            print("SOMEONE TRIED TO LOGIN AND FAILED")
            return HttpResponse("invalid login data")
    
    else:
        print(" USER DIDNT  HIT LOGIN  \n\n\n")
        return render(request,"htmlfiles/loginpage.html", {})


""" la logique qui deconnecte le user """
@login_required
def logoutscenario(request):

    print(" LOGOUT SCENARIO ENTERED  \n\n\n")
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def loginmsgscenario(request):

    print(" LOGIN MSG SCENARIO ENTERED  \n\n\n")
    return HttpResponse("you are logged in ^_^")

