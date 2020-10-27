""" ----------------SCRIPT POUR AJOUTER DES DONNEES DANS LES TABLES----
 """import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project3.settings')

import django
# Import settings
django.setup()

import random
from app3.models import Topic,Webpage,AccessRecord, User
from faker import Faker

#--------------------------------------------------------------------

""" Creation d'un objet Faker()
 """
 fakegen = Faker()

""" une liste de topics dans laquelle on va choisir des topics
au hasard avec la fonction random() """

topics = ['Search','Social','Marketplace','News','Games']

""" La fonction qui permet d'ajouter des topics dans la table Topic
 """def add_topic():
    """ objet t de la table Topic permettant d'inserer des objets Topics
      dans la table Topic"""
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    """ sauvegarder t dans la table """
    t.save()
    return t

"""     retourner t,"""    

"""  la fonction d'insertion des elements dans chaque tables,
  5 par defaut """
def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    """ #Avec la fonction range(), on insert N elements compris entre
    #0 et N exclus """
    for entry in range(N):

        """ # executer la fonction add_topic pour chaque passage
        #de la fonction range() """
        newTopic = add_topic()

        # Create Fake Data for entry
        """ recuper des fakes elements de la class Faker au cours de 
        chaque passage de la fonction range et les stocker dans les tables
        correspondantes """
        newFakeUrl = fakegen.url()
        newFakeDate = fakegen.date()
        newFakeName = fakegen.company()
        newFakeFirstName=fakegen.name()
        newFakeLastname=fakegen.name()
        newFakeEmail=fakegen.email()

        # Create new Webpage Entry
        newWebpage = Webpage.objects.get_or_create(topic=newTopic,url=newFakeUrl,name=newFakeName)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        """ inserer ces elements par le moyen d'objet de chaque table """
        newAccessRecord = AccessRecord.objects.get_or_create(name=newWebpage,date=newFakeDate)[0]
        newUser = User.objects.get_or_create(firstName=newFakeFirstName,lastName=newFakeLastname,email=newFakeEmail)[0]


""" si ce fichier python est execute en ligne de commande sans etre executable
comme importe
populer les tables... """

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
