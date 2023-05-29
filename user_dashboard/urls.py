from django.urls import path
from . import views


urlpatterns = [
    
    path('home/<str:pk>/', views.indexPage, name="user-home"),
    
    path('login/', views.loginPage, name="user-login"),
    path('register/', views.registerPage, name="user-register"), 
    path('logout/', views.logout, name="user-logout"), 
    
    path('profile/edit/<str:pk>/', views.edit_profile, name="user-edit-profile"), 
    
    path('support/<str:pk>/', views.support, name="user-support")
    
    
    
    
]

