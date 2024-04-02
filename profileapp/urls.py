from django.urls import path
from .views import CREATE_PROFILE,PROFILE_VIEW,TUITIONBD ,OTHERPROFILE
urlpatterns = [
    path('create/',CREATE_PROFILE,name='create'),
    path('view/',PROFILE_VIEW, name='view'),
    path('tuitionbd/',TUITIONBD,name='tuitionbd'),
    path('otherprofile/<str:username>/',OTHERPROFILE,name='otherprofile'),
]
