from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .middlewares import auth, guest  
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django import forms
from core.models import UserTemplate


@guest
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('layout')
    else:
        initial_data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
        form = RegistrationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})


@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 


@auth
def logout_view(request):
    logout(request)
    return redirect('/')


# forgot password

class CustomPasswordResetView(PasswordResetView):
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, "We couldn't find an account with that email address.")
            return self.form_invalid(form)
        return super().form_valid(form)
    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm


    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Your password has been set successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error resetting your password.")
        return super().form_invalid(form)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    


    # added code
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required


@login_required
def profile_view(request):
    # Fetch the recent templates for the logged-in user
    recent_templates = UserTemplate.objects.filter(user=request.user).order_by('-date')[:5]

    return render(request, 'userProfile/viewsprofile.html', {
        'recent_templates': recent_templates,
    })


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'userProfile/edit_profile.html', {'form': form})