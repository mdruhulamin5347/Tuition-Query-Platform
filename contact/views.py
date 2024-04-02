from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def CONTACT(request):
    return render(request,'contact.html')


def LOGINPAGE(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid your username and password')
        else:
            messages.error(request, 'invalid your username and password')
    else:
        form=AuthenticationForm()

    return render(request,'login.html', {'form':form})

def LOGOUTPAGE(request):
    logout(request)
    messages.success(request, 'successfully logout the page')
    return redirect('home')

from .forms import UserCreateForm
def SINGUP(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            #get_current=get_current_site(request)
            #mail_subject='An account created'
            #message=render_to_string('account.html',{
                #'user':user,
                #'domain':get_current.domain
            #})
            #send_mail=form.cleaned_data.get('email')
            #email=EmailMessage(mail_subject,message,to=[send_mail])
            #email.send()
            #messages.success(request,'successfully created an account')
            return redirect('/contact/login/')
           
        
    else:
        form=UserCreateForm()
    return render(request, 'singup.html', {'form':form})

def CHANGE(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request,'Successfully change your password')
            return redirect('home')
    else:
        form=PasswordChangeForm(user=request.user)
    return render (request, 'change.html', {'form':form})

    
