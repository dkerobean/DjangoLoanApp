from django.urls import path
from .import views


urlpatterns = [
    path('home/', views.indexPage, name="admin-dashboard"),

    path('all_loans/', views.loanApplicants, name="all-loans"),
    path('loan_application/<str:pk>/', views.viewApplication,
         name="view-loan"),

    path('transaction/', views.viewTransactions, name="transactions"),

    path('edit_profile/<str:pk>/', views.editProfile, name="admin-profile"),

    path('inbox/', views.inbox, name="admin-inbox"),
    path('inbox/read/<str:pk>/', views.viewMessage, name="admin-inbox-read"),

]
