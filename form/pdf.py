from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from form.models import form_model

def render_to_pdf(templete_src, context_dict={}):
    templete=get_template(templete_src)
    html=templete.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None





def contact_pdf(request):
    contact=form_model.objects.all()
    context={
        'contact':contact,
    }
    pdf=render_to_pdf('contact_pdf.html', context)
    if pdf:
        response=HttpResponse(pdf, content_type='application/pdf')
        content='inline; filename=contact.pdf'
        response['Content-Disposition']=content
        return response
    return HttpResponse('not found')