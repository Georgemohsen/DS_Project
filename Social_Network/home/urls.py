from django.urls import path
from . import views


app_name='home'
urlpatterns = [path('', views.status, name='post'),
               path('connect/<str:operation>/<int:pk>/', views.change_friends, name='change_friends'),
               path('like/<int:post_id>/', views.like_posts, name='like_post'),
               path('unlike/<int:post_id>/', views.unlike_posts, name='unlike_post'),]
