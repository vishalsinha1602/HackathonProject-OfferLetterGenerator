from django.db import models
from django.contrib.auth.models import User

class UserTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Ensure this field is not null
    your_name = models.CharField(max_length=100)
    your_address = models.CharField(max_length=255)
    city_state_zip = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    website = models.URLField(blank=True)
    date = models.DateField()
    recipient_name = models.CharField(max_length=100)
    recipient_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_city_state_zip = models.CharField(max_length=100)
    your_title = models.CharField(max_length=50)
    content = models.TextField()
    
