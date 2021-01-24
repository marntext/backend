from django.urls import path
from .views import category_list, like, post_list, post_create, post_detail, post_get_update_delete, comment_create_view, comment_edit_view
#from .views import comment_list

urlpatterns = [
    path("category-list/", category_list),
    path("post-list/", post_list),
    path("post-create/", post_create),
    path("<str:slug>/post-detail/", post_detail),
    #path("comment-list/", comment_list),
    path("<str:slug>/edit/", post_get_update_delete),
    path("<str:slug>/comment-create/", comment_create_view),
    path("<str:slug>/<int:id>/comment-edit/", comment_edit_view),
    path("<str:slug>/like/", like),
]
