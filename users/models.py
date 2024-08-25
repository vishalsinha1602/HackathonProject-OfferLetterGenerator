from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
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
