"""digital_contract URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

# custom views
from home.views import Home, UserVerification
from account.views import Account

urlpatterns = [
    path('', Home.as_view(), name='home'), # index page
    path('<verification_token>', UserVerification.as_view(), name='new_user_verification'),
    path('account/', Account.as_view(), name='account'), # user's account
    path('admin/', admin.site.urls, name='admin'),
]
