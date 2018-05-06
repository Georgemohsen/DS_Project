from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [path('signup/', views.signup_view, name="sign_up"),
               path('login/', views.login_view, name="login"),
               path('logout/', views.logout_view, name="logout"),
               path('profile/', views.profile_view, name="profile"),
               path('profile/<int:pk>/', views.profile_view, name="profile_with_pk"),
               path('editProfile/', views.edit_profile, name="editProfile"),
               path('friends/', views.user_friends, name="friends")]
