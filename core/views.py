from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import CoverLetterForm
from .models import UserTemplate
from users.middlewares import auth
from django.utils import timezone
from datetime import timedelta
import pdfkit


path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def create_letter(request):
    return render(request, 'Offer_letter_page.html')

@auth
def generate_cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line
            data = form.cleaned_data

            # Generate a meaningful name for the template
            template_name = "Offer Letter - " + data.get('your_name', 'Unnamed')

            # Save the template data to the database
            user_template = UserTemplate(
                user=request.user,
                name=template_name,
                your_name=data['your_name'],
                your_address=data['your_address'],
                city_state_zip=data['city_state_zip'],
                phone_number=data['phone_number'],
                email_address=data['email_address'],
                website=data.get('website', ''),
                date=data['date'],
                recipient_name=data['recipient_name'],
                recipient_title=data['recipient_title'],
                company_name=data['company_name'],
                company_address=data['company_address'],
                company_city_state_zip=data['company_city_state_zip'],
                your_title=data['your_title'],
                content=render_to_string('TemplatesForms/form_1/description.html', {'data': data})
            )
            user_template.save()
            messages.success(request, 'Template saved successfully!', extra_tags='template_view')
            return redirect('view_offer_letter')  # Redirect to view templates
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        print("Request method is not POST")
    
    return render(request, 'Offer_letter_page.html', {'form': form})



@auth
def view_offer_letter(request):
    # Fetch all templates for the logged-in user
    templates = UserTemplate.objects.filter(user=request.user)
    
    # Calculate recent date (e.g., last 30 days)
    recent_date = timezone.now() - timedelta(days=30)
    recent_templates = templates.filter(date__gte=recent_date)
    
    return render(request, 'view_offer_letter.html', {
        'templates': templates,
        'recent_templates': recent_templates,
    })



def render_to_pdf(template_src, context_dict={}):
    # Render HTML template with context
    html_string = render_to_string(template_src, context_dict)
    
    # Convert HTML to PDF using pdfkit
    pdf = pdfkit.from_string(html_string, False)
    
    # Return the PDF as an HTTP response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Offer_letter.pdf"'
    return response

def download_pdf(request, pk):
    # Fetch the template based on the provided ID and the current user
    user_template = get_object_or_404(UserTemplate, pk=pk, user=request.user)

    # Generate the PDF using the template and context data
    context = {
        'data': {
            'name': user_template.name,
            'your_name': user_template.your_name,
            'your_address': user_template.your_address,
            'city_state_zip': user_template.city_state_zip,
            'phone_number': user_template.phone_number,
            'email_address': user_template.email_address,
            'website': user_template.website,
            'date': user_template.date,
            'recipient_name': user_template.recipient_name,
            'recipient_title': user_template.recipient_title,
            'company_name': user_template.company_name,
            'company_address': user_template.company_address,
            'company_city_state_zip': user_template.company_city_state_zip,
            'your_title': user_template.your_title,
            'content': user_template.content  # Always use the latest content
        }
    }

    # Render to PDF
    response = render_to_pdf('LetterTemplates/template1.html', context)
    return response
    
    # Return the generated PDF as an HTTP response
    return response

@auth
def delete_offer_letter(request, pk):
    # Get the template by primary key
    template = get_object_or_404(UserTemplate, pk=pk, user=request.user)

    # Delete the template
    template.delete()

    # Add a success message
    messages.success(request, 'Template deleted successfully!', extra_tags='delete_message')

    # Redirect back to the view templates page
    return redirect('view_offer_letter')

from .forms import UserTemplateForm

def edit_offer_letter(request, pk):
    template = get_object_or_404(UserTemplate, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = UserTemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            messages.success(request, 'Template updated successfully!')
            return redirect('view_offer_letter')
        else:
            # Debugging: Print form errors to console
            print("Form is not valid")
            print(form.errors)
    else:
        form = UserTemplateForm(instance=template)
    
    return render(request, 'edit_offer_letter.html', {'form': form})