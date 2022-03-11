from django.urls import path
from .import views


urlpatterns = [
    path('', views.main ,name='main'),
    path('create/',views.create.as_view(),name='create'),
    path('view/',views.all.as_view(),name='all'),
    # path('view/<int:pk>', views.detail.as_view(),name='detail')
    path('update/<int:pk>', views.update.as_view(),name='update'),
    path('delete/<int:pk>', views.delete.as_view(),name='delete'),
    path('forums/',views.forum.as_view(),name='forum'),
    path('forums/create',views.forum_create.as_view(),name='forum_create'),
    path('forums/detail/<int:pk>',views.forum_detail.as_view(),name='forum_detail'),
    path('forums/comments/create/<int:pk>',views.create_comment.as_view(),name="create_comment"),
    path('forums/comments/delete/<int:pk>',views.forum_comment_delete.as_view(),name='forum_comment_delete'),
    path('forums/delete/<int:pk>',views.forum_delete.as_view(),name='forum_delete'),


    path('review/', views.give_review.as_view(),name="review"),





]
