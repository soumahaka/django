from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
CreateView, UpdateView, DeleteView)
from .models import School, Student


#la listview pour lister les donnees d'une table
class SchoolListView(ListView):

    """ context_object_name est le nom de la list creee par django,
    a la base il prend le nom de la table associee et il le lower en ajoutant 
    _list, ici on l'a modifie en donnant notre propre nom """

    context_object_name="schools"
    #juste on connecte la table a model pour creer la liste
    model=School


#la detailview qui permet de donner les details d'une innstance 
#dans la table
class SchoolDetailView(DetailView):

    """ context_object_name est le nom de la Detail creee par django,
    a la base il prend le nom de la table et il le lower en ajoutant , 
    ici on l'a modifie en donnant notre propre nome """

    context_object_name='schooldetail'
    model=School


#ces class sont associees a des tables et des fichiers html de types nom de la table _list.html
#et nom de la table _detail.html et nom de la table _confirm_delete 
# dans un dossier de nom le nom de l'application
class SchoolCreateView(CreateView):
    model=School
    fields="__all__"


class SchoolUpdateView(UpdateView):
    model=School
    fields=("name", "principal")

    #success_url="" permet de rediriger l'utilisateur a une page de notre choix


class SchoolDeleteView(DeleteView):
    """ context_object_name est le nom des instance de la table a delete creee par django,
    a la base il prend le nom de la table associee et il le lower, """
    model=School
    success_url="/"    



""" class Homescenario(TemplateView):
utilisation la plus simple possible d'une class based view
on indique juste au template name le fichier html a affichier
    template_name="homepage.html" """

""" redefinition de la fonction qui retourne les donnees du dictionnaire comme
dans les views qu'on injecte dans du htmls"""
""" def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["injection"]="basic templateview"
        return context """

