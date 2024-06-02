from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allposts', views.all_posts, name='all-posts'),
]
