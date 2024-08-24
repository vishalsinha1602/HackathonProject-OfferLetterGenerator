from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .middlewares import auth, guest  
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render


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
