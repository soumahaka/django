from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

#creation des tables dans la base de donnees qui vont contenir 
# les informations a manipuler sur notre


#la table Post qui enregistre l'auteur, le titre, le text,
#la date de creation du post, la date de publication du post

#ici l'auther est uniquement le superuser
class Post(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    #fonction assoiciee a cette table qui permet d'agir
    #sur les instances de Post en mettant published_date a timezone.now()
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #fonction qui retourne les commentaitre ou approved_comment est true dans 
    # la table Comment
    #en effet, comments represente une instance de Comment accessible a Post
    #par la relation de cle etrangere dans Comment

    #Comment a acces aux elements de Post et Post a acces aux elements de 
    # Comment, c'est la l'utilite de related_name
    

    #cette fonction retourne tous les comment ou approved_comment=True
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    #fonction qui permet de rediriger l'utilisateur vers detail-post-page
    #de son post apres avoir fait un post
    def get_absolute_url(self):
        return reverse("detail-post-page",kwargs={'pk':self.pk})

    
    #fonction qui retourne le titre d'un post
    def __str__(self):
        return self.title


#Table Comment qui enregistre un text, l'auteur, un post, la date de creation,
#une approbation(coche, ou non)
class Comment(models.Model):
    post=models.ForeignKey("blogapp.Post", related_name="comments", on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)


    #fonction qui permet de mettre approved_comment a true
    def approve(self):
        self.approved_comment=True
        self.save()

    #fonction qui retourne le text d'un comment
    def __str__(self):
        return self.text