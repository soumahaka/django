from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    location=models.CharField(max_length=256)

    def __str__(self):
        return self.name


    #cette methode permet de rediriger le user a la detailpage quand il fini
    #de modifier ses donnees pour voir les modifications qu'il a apporte sur
    #l'instance particuliere

    def get_absolute_url(self):
        return reverse("schooldetail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()

    #quand on dit foreignKey, c'est une instance d'une autre table
    #necessaire dans une autre
    school=models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name