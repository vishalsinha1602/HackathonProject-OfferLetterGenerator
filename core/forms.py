from django import forms


class CoverLetterForm(forms.Form):
    your_name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Dr. Elana Mohammad, MD'})
    )
    your_address = forms.CharField(
        label='Your Address',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': '9436 Feather Street'})
    )
    city_state_zip = forms.CharField(
        label='City, State, ZIP Code',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Satyagiri, New Delhi'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '+91 12345 67890'})
    )
    email_address = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'placeholder': 'hello@reallygreatsite.com'})
    )
    website = forms.URLField(
        label='Website (if any)',
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'www.reallygreatsite.com'})
    )
    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    recipient_name = forms.CharField(
        label='Recipient\'s Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Muhammad Patel'})
    )
    recipient_title = forms.CharField(
        label='Recipient\'s Title',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Recruitment Consultant'})
    )
    company_name = forms.CharField(
        label='Company Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'The Penshaw Medical Center'})
    )
    company_address = forms.CharField(
        label='Company Address',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': '77 Satya Giri Complex, Phalke Road'})
    )
    company_city_state_zip = forms.CharField(
        label='Company City, State, ZIP Code',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Mumbai, Maharashtra 8754'})
    )
    your_title = forms.CharField(
        label='Your Title',
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'MD'})
    )



from .models import UserTemplate

class UserTemplateForm(forms.ModelForm):
    class Meta:
        model = UserTemplate
        fields = [
            'name', 'your_name', 'your_address', 'city_state_zip',
            'phone_number', 'email_address', 'website', 'date',
            'recipient_name', 'recipient_title', 'company_name',
            'company_address', 'company_city_state_zip', 'your_title',
            'content'
        ]


