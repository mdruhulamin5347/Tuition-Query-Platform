from django.urls import path
from .views import FORM
from .pdf import contact_pdf

urlpatterns = [
    path('',FORM.as_view(),name=''),
    path('pdf/',contact_pdf, name='pdf'),
]
