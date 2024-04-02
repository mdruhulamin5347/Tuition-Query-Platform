from django.urls import path
from .views import LOGINPAGE,LOGOUTPAGE,SINGUP,CONTACT,CHANGE


urlpatterns = [
    path('',CONTACT),
    path('login/',LOGINPAGE,name='login'),
    path('logout/',LOGOUTPAGE),
    path('singup/',SINGUP),
    path('change/',CHANGE),

  
]
