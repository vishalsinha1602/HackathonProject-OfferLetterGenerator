from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.urls import reverse_lazy
from django import forms


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
    
    # added code

from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-full px-4 py-2 border rounded'})
        self.fields['email'].widget.attrs.update({'class': 'w-full px-4 py-2 border rounded'})
        self.fields['first_name'].widget.attrs.update({'class': 'w-full px-4 py-2 border rounded'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full px-4 py-2 border rounded'})
