from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class ExtendedUser(models.Model):
  print(__name__ +" GOT CALLED !"+"\n\n\n")


  """ code qui dit que nous voulons utiliser les champs de User de django """
  linkedToUser=models.OneToOneField(User,on_delete=models.CASCADE)

  """ nos champs de surplus ajoutes a ceux de User """
  WebSite=models.URLField(blank=True)

  Picture=models.ImageField(upload_to='photos',blank=True)
  
  
  """ Affiche les info des utilisateur dans la partie admin selon l'attribut specifie """
  def __str__(self):
    return self.linkedToUser.username
