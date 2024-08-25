from django.urls import path 
from django.contrib.auth.decorators import login_required
from . import views



urlpatterns = [
    path('dashboard/', login_required(views.dashboard_view), name='layout'),
    path('create-templates/', login_required(views.create_template), name='create_templates'),
    path('cover-letter/', login_required(views.generate_cover_letter), name='generate_cover_letter'),
    # Remove the save_form_data URL
    # Remove the download_pdf URL
    path('download_pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('delete_template/<int:pk>/', views.delete_template, name='delete_template'),
    path('view-templates/', login_required(views.view_templates), name='view_templates'),
]
