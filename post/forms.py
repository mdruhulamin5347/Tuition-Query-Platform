from django import forms
from .models import post_model,photo_add_model
from django.forms import CheckboxSelectMultiple
from .fields import ListTextWidget

class post_form(forms.ModelForm):
    class Meta:
        model=post_model
        exclude=['user','id','slug','create_at','likes','views']
        widgets={
            'teacher':CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'student':CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }
    def __init__(self, *args, **kwargs):
        _district_set=kwargs.pop('district_set',None)
        super(post_form,self).__init__(*args, **kwargs)
        self.fields['district'].widget=ListTextWidget(data_list=_district_set,name='district')

class photo_add_form(forms.ModelForm):
    class Meta:
        model=photo_add_model
        fields=['image']