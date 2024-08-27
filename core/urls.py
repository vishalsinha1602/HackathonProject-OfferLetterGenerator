from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views



urlpatterns = [
    path('dashboard/', login_required(views.dashboard_view), name='layout'),
    path('create-letter/', login_required(views.create_letter), name='create_letter'),
    path('cover-letter/', login_required(views.generate_cover_letter), name='generate_cover_letter'),
     path('edit_offer_letter/<int:pk>/', views.edit_offer_letter, name='edit_offer_letter'),
    # Remove the save_form_data URL
    # Remove the download_pdf URL
    path('download_pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('delete_offer_letter/<int:pk>/', views.delete_offer_letter, name='delete_offer_letter'),
    path('view_offer_letter/', login_required(views.view_offer_letter), name='view_offer_letter'),
    
    

 

]
