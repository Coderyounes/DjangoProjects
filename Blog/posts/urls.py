from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all_posts, name='all-posts'),
    path('add', views.add_post, name='add_post'),
    path('update/<str:pk>', views.update_post, name='update_post'),
]
