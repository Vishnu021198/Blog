from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/share/', views.share_blog, name='share_blog'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('tag/<str:tag_name>/', views.tag_search, name='tag_search'),
]
