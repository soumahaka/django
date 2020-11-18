from django.shortcuts import render
from blogapp.models import Post, Comment
from django.views.generic import (TemplateView, ListView,
UpdateView, DeleteView, DetailView, CreateView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

#la plus simple vue possible, affichage d'un fichier html avec
#template_name
class AboutView(TemplateView):
    template_name="about.html"


#CBV qui retourne toutes les instances de Post avec son queryset
#elle necessite un fichier html de type model_list.html dans
#blogapp/templates/blogapp/

class PostListView(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()
        ).order_by("-published_date")#la date la plus recente
    


#CBV qui affiche les details d'une instance de post
##elle necessite un fichier html de type model_detail.html dans
#blogapp/templates/blogapp/

class PostDetailView(DetailView):
    model=Post
    

#CBV qui permet de creer un post par le biais de sa form associee
##elle necessite un fichier html de type model_form.html dans
#blogapp/templates/blogapp/
class PostCreateView(LoginRequiredMixin,CreateView):
    
    #login_url="/login/"
    
    redirect_field_name="blogapp/post_detail.html" #rediriger le user 
    #sur cette page apres avoir creer un post
    
    form_class=PostForm 
    model=Post


#CBV qui permet de update un post par le biais de sa form associee
##elle necessite un fichier html de type model_form.html dans
#blogapp/templates/blogapp/
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url="/login/"
    redirect_field_name="blogapp/post_detail.html"
    form_class=PostForm
    model=Post


#CBV qui permet de delete un post
##elle necessite un fichier html de type model_confirm_delete.html dans
#blogapp/templates/blogapp/
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    success_url="/"

#CBV qui retourne les instance de Post avec son queryset pour faire du draftlist
##elle necessite un fichier html de type model_draft_list.html dans
#blogapp/templates/blogapp/
class DraftPostListView(LoginRequiredMixin, ListView):
    #login_url="/login/"
    #redirect_field_name="blogapp/post_list.html" #redirection
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("create_date")
    



#######################################
## Functions that require a pk match ##
#######################################

#les fonctions performees dans le site

#publier un post, il s'agit de set son published_date a timezone.now()

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('detail-post-page', pk=pk)

#fonction ajouter un commentaire a un post tres complex
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail-post-page', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogapp/comment_form.html', {'form': form})

#fonction approuver un commentaire
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail-post-page', pk=comment.post.pk)

#supprimer un commentaire
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('detail-post-page', pk=post_pk)