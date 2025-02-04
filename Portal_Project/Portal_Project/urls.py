"""
URL configuration for Portal_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
"""
URL configuration for Portal_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# """
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from Portal_App import views
from Portal_App.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.INDEX,name="home"),
    path('create',views.CREATE,name="create"),
    path('login',views.Login,name="login"),
    path('forgot',views.Forgot, name="forgot"),
    path('OtpVerify',views.OtpVerify,name="OtpVerify"),
    path('changepassword', ChangePassword.as_view(), name='changepassword'),
]
# from django.contrib import admin
# from django.urls import path
# from Portal_App import views
# from Portal_App.views import *
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.INDEX,name="home"),
#     path('create',views.CREATE,name="create"),
#     path('login',views.Login,name="login"),
#     path('forgot',views.Forgot, name="forgot"),
#     path('validate_otp', views.OtpVerify, name="validate_otp"),
#     path('changepassword', ChangePassword.as_view(), name="changepassword"),
# ]