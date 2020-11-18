from django.urls import path
from blogapp import views

#Mappage de urls des views
urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list-page"),
    path("about/", views.AboutView.as_view(), name="about-page"),
    path("post-list/", views.PostListView.as_view(), name="post-list-page"),
    path("create-post/", views.PostCreateView.as_view(), name="create-post-page"),
    path("detail-post/<int:pk>/", views.PostDetailView.as_view(), name="detail-post-page"),
    path("update-post/<int:pk>/", views.PostUpdateView.as_view(), name="update-post-page"),
    path("delete-post/<int:pk>/", views.PostDeleteView.as_view(), name="delete-post-page"),
    path("drafts-post/", views.DraftPostListView.as_view(), name="draft-post-page"),
    path("add-comment/<int:pk>/", views.add_comment_to_post, name="add-comment-page"),
    path("approve-comment/<int:pk>/", views.comment_approve, name="approve-comment-page"),
    path("remove-comment/<int:pk>/", views.comment_remove, name="remove-comment-page"),
    path("publish-post/<int:pk>/", views.post_publish, name="publish-post-page"),
]
