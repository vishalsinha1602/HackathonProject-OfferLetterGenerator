from django.contrib import admin
from .models import UserTemplate

class UserTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'your_name', 'date', 'company_name')
    search_fields = ('your_name', 'recipient_name', 'company_name')

admin.site.register(UserTemplate, UserTemplateAdmin)

