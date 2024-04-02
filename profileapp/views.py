from django.shortcuts import render,redirect
from .forms import userprofile_form,teacher_form
from .models import userprofile_model,teacher_model
from django.contrib import messages

# Create your views here.
def CREATE_PROFILE(request):
    try:
        instance=userprofile_model.objects.get(user=request.user)
    except userprofile_model.DoesNotExist :
        instance=None
    if request.method=="POST":
        if instance:
            form=userprofile_form(request.POST, request.FILES, instance=instance)
        else:
            form=userprofile_form(request.POST, request.FILES)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'successfully created your profile')
            return redirect('home')
    else:
        form=userprofile_form(instance=instance)
    return render(request, 'new/profile.html',{'form':form})

def PROFILE_VIEW(request):
    user=request.user
    return render(request,'new/profile_view.html',{'user':user})



def TUITIONBD(request):
    try:
        instance=teacher_model.objects.get(user=request.user)
    except :
        instance=None
    if request.method=="POST":
        if instance:
            form=teacher_form(request.POST,instance=instance)
        else:
            form=teacher_form(request.POST,)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()            
            messages.success(request,'successfully created your profile')
            return redirect('home')
            
    else:
        form=teacher_form(instance=instance)
    return render(request, 'new/teacher.html',{'form':form})

from .models import User
def OTHERPROFILE(request,username):
    user=User.objects.get(username=username)
    return render(request,'new/otherprofile.html',{'user':user})