from django.shortcuts import render
from users.middlewares import auth, guest 
from django.http import HttpResponse
from .forms import CoverLetterForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa 
from io import BytesIO




# Create your views here.
@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')
  


@auth
def generate_cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            data = form.cleaned_data

            # Render the cover letter template with the user input
            return render(request, 'saveChangesform/form1.html', {'data': data})

    else:
        form = CoverLetterForm()

    return render(request, 'cover_letter_page.html', {'form': form})



from datetime import date


def save_form_data(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            # Convert date objects to string format
            if 'date' in cleaned_data and isinstance(cleaned_data['date'], date):
                cleaned_data['date'] = cleaned_data['date'].isoformat()

            # Save form data to the session
            request.session['form_data'] = cleaned_data

            # Optional: Log the saved data to verify
            # print("Saved data:", cleaned_data)

            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

# Utility function to render a PDF from a given HTML template

def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(template.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cover_letter.pdf"'
        return response
    return None
# View to handle the download of the generated PDF

def download_pdf(request):
    # Get form data from session
    form_data = request.session.get('form_data', {})

    # Generate the PDF
    response = render_to_pdf('saveChangesform/form1.html', {'data': form_data})

    # Clear the session data after generating the PDF
    if 'form_data' in request.session:
        del request.session['form_data']

    return response