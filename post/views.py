from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import post_model,Teacher,Student,Comment,photo_add_model,District
from .forms import post_form,photo_add_form
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .templatetags import tag

# Create your views here.
'''
class POST(CreateView):
    model=post_model
    form_class=post_form
    template_name='post.html'
    success_url='/home/'
    def form_valid(self, form):
        form.save()
        form.instance.User=self.request.user
        return super().form_valid(form)

from profileapp.models import teacher_model
def receiverchoose(j,object):
    count= 0
    if j.district==object.district:
        count= count + 1
    for i in j.medium:
        for k in object.middle:
            if i == k:
                count = count + 1
                break
    for i in j.subject_in.all():
        for j in object.teacher.all():
            if i==j:
                count = count + 1
                break
    for i in j.class_in.all():
        for k in object.student.all():
            if i==k:
                count = count + 1
                break
    if count >= 1:
        return True

     
                us=teacher_model.objects.all()
                for i in us:
                    if receiverchoose(i,object):
                        receiver=i.user
                        if receiver != request.user:
                            notify.send(request.user, recipient=receiver, verb="has searching a teacher like you" + f''<a href="/post/details/{object.id}"> Go </a>'')


    
'''

def POST(request):
    if request.method=='POST':
        form=post_form(request.POST , request.FILES)
        if form.is_valid():
            object=form.save(commit=False)
            object.user=request.user
            object.save()
            dis=form.cleaned_data['district']
            if not District.objects.filter(name=dis).exists():
                disobj=District(name=dis)
                disobj.save()
            sub=form.cleaned_data['student']
            for s in sub:
                object.student.add(s)
                object.save()
            tc=form.cleaned_data['teacher']
            for t in tc:
                object.teacher.add(t)
                object.save()
            messages.success(request,'successfully submited your post')
            return redirect('home')
    else:
        form=post_form(district_set=District.objects.all().order_by('name'))  
    return render(request,'post.html',{'form':form})




    

class LIST(ListView):
    template_name='list.html'
    queryset=post_model.objects.all()

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data( *args, **kwargs)
        context['posts']=context.get('object_list')
        context['teachers']=Teacher.objects.all()
        context['students']=Student.objects.all()  
        return context

class DETAILS(DetailView):
    model=post_model
    template_name='details.html'
    def get_context_data(self,*args, **kwargs):
        self.object.views.add(self.request.user)
        liked=False
        if self.object.likes.filter(id=self.request.user.id).exists():
            liked=True
        context=super().get_context_data(*args,**kwargs)
        object=context.get('object')
        comments=Comment.objects.filter(post=object.id,parent=None)
        replies=Comment.objects.filter(post=object.id).exclude(parent=None)
        dictofreplay={}
        for replay in replies:
            if replay.parent.id not in dictofreplay.keys():
                dictofreplay[replay.parent.id]=[replay]
            else:
                dictofreplay[replay.parent.id].append(replay)

        context['comments']=comments
        context['dictofreplay']=dictofreplay
        context['liked']=liked
        return context
from notifications.signals import notify
from django.http import HttpResponseRedirect
def LIKEPOST(request,id):
    if request.method=='POST':
        post=post_model.objects.get(id=id) 
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            if request.user != post.user:
                notify.send(request.user , recipient=post.user, verb="has liked your post" + f'''<a href="/post/details/{post.id}"> Go </a>''')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def NOTIFICATION_R(request):
    return render(request,'notifications.html')



class EDIT(UpdateView):
    model=post_model
    form_class=post_form
    template_name='post.html'
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('details', kwargs={'pk':id})
    
#class DELETE(DeleteView):
#   model=post_model
#   template_name='details.html'
#    success_url='/post/list/'

def DELETE(request,id):
    post=post_model.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/post/list/')
   




def SEARCH(request):
    query=request.POST.get('search', ' ')
    if query:
        queryset= (Q(title__icontains=query)) | (Q(salary__icontains=query)) | (Q(details__icontains=query)) | (Q(middle__icontains=query)) | (Q(catagory__icontains=query)) | (Q(teacher__name__icontains=query)) | (Q(student__name__icontains=query))
        results=post_model.objects.filter(queryset).distinct()

    else:
        results=[ ]
    return render (request, 'search.html', {'results':results})

def FILTER(request):
    request.method='POST'
    teacher=request.POST['teacher']
    student=request.POST['student']
    available=request.POST['available']
    salary_from=request.POST['salary_from']
    salary_to=request.POST['salary_to']
    if teacher or student:
        queryset= (Q(teacher__name__icontains=teacher)) & (Q(student__name__icontains=student))
        results=post_model.objects.filter(queryset).distinct()
        if available:
            results=results.filter(available=True)
        if salary_from:
            results=results.filter(salary__gte=salary_from)
        if salary_to:
            results=results.filter(salary__lte=salary_to)
    else:
        results=[ ]
    return render (request, 'search.html', {'results':results})


def COMMENT(request):
    if request.method=="POST":
        comment=request.POST['comment']
        parentid=request.POST['parentid']
        postid=request.POST['postid']
        post=post_model.objects.get(id=postid)
        if parentid:
            parent=Comment.objects.get(id=parentid)
            newcom=Comment(text=comment, user=request.user, post=post,parent=parent)
            newcom.save()
        else:
            newcom=Comment(text=comment, user=request.user, post=post)
            newcom.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def DELETECOMMENT(request,id):
    comment=Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))






def PICADD(request,id):
    post=post_model.objects.get(id=id)
    if request.method=='POST':
        form=photo_add_form(request.POST, request.FILES)
        if form.is_valid():
            image=form.cleaned_data['image']
            obj=photo_add_model(image=image, post=post)
            obj.save()
            messages.success(request,'Successfully uploaded your picture')
            return redirect(f"/post/details/{id}")
        
    else:
        form=photo_add_form()

    contain={
        'form':form,
        'id':id,
    }
    return render(request,'picadd.html',contain)
            
def APPLY(request, id):
    post=post_model.objects.get(id=id)
    notify.send(request.user , recipient=post.user, verb="has apply tuition for you" + f'''<a href="/profileapp/otherprofile/{request.user.username}"> Go </a>''')
    messages.success(request, "your request succesfully sumited")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


import requests
import json
def postviews(request):
    api_intregation=requests.get("https://jsonplaceholder.typicode.com/posts")
    try:
        api=json.loads(api_intregation.content)
    except:
        api="Error"
    return render(request,"postviews.html", {'api':api})