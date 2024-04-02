from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import form_form
from django.contrib import messages

# Create your views here.
class FORM(FormView):
    form_class=form_form
    template_name='form.html'
    success_url='../home/'
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Message is successfully submited')
        redirect('form')
        return super().form_valid(form)

    
        



    
