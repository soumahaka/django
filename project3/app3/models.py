'''Importations tres necessaires pour creer des tables'''

from django.db import models

# Create your models here.

'''Creation des differentes tables de la base de donnee deja existante 
dans django
'''

'''table Topic avec une seule colonne de donnees 'topic_name''''
class Topic(models.Model):
    topic_name=models.CharField(max_length=255,unique=True)

    '''la methode string qui retourne les donnee de cette table'''
    def __str__(self):
        return self.topic_name

'''la table Webpage avec trois colonnes de donnees'''
class Webpage(models.Model):

    '''un objet de la table topic est necessaire dans la table
    Webpage qui apparait comme cle etrangere'''

    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):

    '''un objet de la table Webpage est necessaire dans la table
    AccessRecord qui apparait comme cle etrangere'''
    
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.date

class User(models.Model):
    firstName=models.CharField(max_length=255, unique=True)
    lastName=models.CharField(max_length=255, unique=True)
    email=models.EmailField(unique=True)
    #verifyEmail=models.EmailField(unique=True, null=True)

    def __str__(self):
        return str(self.firstName) + " "+str(self.lastName)+ " "+str(self.email)
        