from django.urls import path
from . import views


urlpatterns = [
    
    path('home/', views.indexPage, name="user-home"),
    
    path('login/', views.loginPage, name="user-login"),
    path('register/', views.registerPage, name="user-register"), 
    
    
]

