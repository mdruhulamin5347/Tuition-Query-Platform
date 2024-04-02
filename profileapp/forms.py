from django import forms
from .models import userprofile_model,teacher_model
from django.forms import CheckboxSelectMultiple

class userprofile_form(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=userprofile_model
        exclude=('user',)


class teacher_form(forms.ModelForm):
    class Meta:
        model=teacher_model
        exclude=('user',)
        widgets={
            'subject_in':CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'class_in':CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }
