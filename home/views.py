from django.shortcuts import render
from django.views.generic import ListView
from post.models import post_model

# Create your views here.
class HOME(ListView):
    model=post_model
    template_name='home.html'


