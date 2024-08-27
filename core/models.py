from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models
import os



class UserTemplate(models.Model):
    from .views import user_directory_path
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
    content = HTMLField()  # Use HTMLField for rich text content
    pdf = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.pdf:
            if os.path.isfile(self.pdf.path):
                os.remove(self.pdf.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return  self.name
    
