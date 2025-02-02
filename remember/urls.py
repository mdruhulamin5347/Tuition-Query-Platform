"""remember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from contact.views import LOGINPAGE
from home.views import HOME
from post.views import LIST
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',HOME.as_view(), name=''),
    #path('',LOGINPAGE,name=''),
    path('',LIST.as_view(),name='home'),
    #path('home/',LIST.as_view(),name='home'),
    #path('home/',HOME.as_view(), name='home'),
    path('form/',include('form.urls'), name='form'),
    path('contact/',include('contact.urls'), name='contact'),
    path('post/',include('post.urls'), name='post'),
    path('profileapp/',include('profileapp.urls'), name='profileapp'),
    path('inbox/notifications/',include('notifications.urls', namespace='notifications')),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
