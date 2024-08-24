from django import forms
from .views import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.urls import reverse_lazy

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
    


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True)



class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        """If the form is valid, send a success message."""
        messages.success(self.request, "A reset email has been sent to the provided email address.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, check if the email exists, and send an error message."""
        email = form.cleaned_data.get('email')
        if email and not User.objects.filter(email=email).exists():
            messages.error(self.request, "We couldn't find an account with that email address.")
        return super().form_invalid(form)
    
    