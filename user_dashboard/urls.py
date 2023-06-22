from django.urls import path
from . import views


urlpatterns = [
    
    path('home/', views.indexPage, name="user-home"),
    
    path('login/', views.loginPage, name="user-login"),
    path('register/', views.registerPage, name="user-register"), 
    path('logout/', views.logout, name="user-logout"), 
    
    path('profile/edit/<str:pk>/', views.edit_profile, name="user-edit-profile"), 
    
    path('support/<str:pk>/', views.support, name="user-support"),
    
    path('verify_payment/<str:reference>/<int:amount>/', views.verifyPayment, name="verify-payment"),
    
    path('transactions/<str:pk>/', views.showTransactions, name="user-transactions"), 
    
    path('wallet/<str:pk>/', views.myWallet, name="user-wallet"), 
    
    path('loan/<str:pk>/', views.userLoans, name="user-loans"), 
    
    path('inbox/<str:pk>/', views.userInbox, name="user-inbox"),   
    
]

