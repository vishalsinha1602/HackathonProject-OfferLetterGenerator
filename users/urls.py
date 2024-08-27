from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views  
# Import your custom views

urlpatterns = [
    # User Registration
    path('register/', views.register_view, name='register'),

    # User Login
    path('login/', views.login_view, name='login'),

    # User Logout
    path('logout/', views.logout_view, name='logout'),

    # Password Reset - Request (Custom)
    path('password_reset/', 
         views.CustomPasswordResetView.as_view(template_name='auth/password_reset_form.html'), 
         name='password_reset'),

    # Password Reset - Email Sent Confirmation (Default)
    path('password_reset_done/',views.CustomPasswordResetView.as_view(template_name='auth/password_reset_email.html'), 
         name='password_reset_done'),

    # Password Reset - Confirm (Custom)
    path('password_reset_confirm/<uidb64>/<token>/', 
         views.CustomPasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),

    # Password Reset - Complete (Default)
    path('password_reset_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_form.html'), 
         name='password_reset_complete'),

     #     added code

     path('profile/',views.profile_view, name='profile'),
     path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]
     