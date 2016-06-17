"""elastidjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    
    
Created on May 16, 2016
@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

from django.conf.urls import url, include
from django.contrib import admin
from core import views 
# from account import views as account_views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),    
    url(r'^admin/', admin.site.urls),
    url(r'^search/', views.search_view, name='search'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^apps/core/', include('core.urls')),
    url(r'^apps/account/', include('account.urls')),
]
