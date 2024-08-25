from django.urls import path 
from django.contrib.auth.decorators import login_required
from . import views



urlpatterns = [
    path('dashboard/', login_required(views.dashboard_view), name='layout'),
    path('cover-letter/', login_required(views.generate_cover_letter), name='generate_cover_letter'),
    path('save_form_data/', login_required(views.save_form_data), name='save_form_data'),
    path('download_pdf/', login_required(views.download_pdf), name='download_pdf'),
]
