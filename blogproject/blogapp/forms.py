from django import forms
from .models import Post, Comment

#Les form derivees des tables de notre base de donnees qui vont
#prendre les informations de l'utilisateur pour les mettre dans nos tables

#la form d'un post avec 3 champs(author, titre, text)
class PostForm(forms.ModelForm):


    class Meta():
        model=Post
        fields=("author", "title", "text")
        
        #widget permet de mettre du style css aux elements des form en leur
        #donnant des class
        widgets={"title":forms.TextInput(attrs={"class": "textinputclass"}),
        "text":forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"})


        }

#la form d'un comment avec 2 champs(author, text)
class CommentForm(forms.ModelForm):
    
    class Meta():
        model=Comment
        fields=("author", "text")

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }