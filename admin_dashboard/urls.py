from django.urls import path
from .import views


urlpatterns = [
    path('home/', views.indexPage, name="admin-dashboard"), 
    
    path('all_loans/', views.loanApplicants, name="all-loans"),
    path('loan_application/<str:pk>/', views.viewApplication, name="view-loan"),
]
