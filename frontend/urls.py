from django.urls import path
from . import views

urlpatterns = [

    path('', views.indexPage, name="index-page"),

    path('get_loan/', views.getLoan, name="get-loan"),
    path('loan/', views.loanApplication, name="loan-application"),
    path('loan_details/', views.loanDetails, name="loan-details"),
    path('personal_details/', views.personalDetails, name="personal-details"),
    path('document_upload/', views.documentUpload, name="document-upload"),

    path('contact/', views.contact, name="contact")
]
