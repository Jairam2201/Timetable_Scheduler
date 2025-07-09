"""
URL configuration for project_1 project.

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
from django.contrib import admin
from django.urls import path
from .views import forgot_password,password_reset,view,time_table,signup,login,user_login,user_signup,date,edit,insert,save_work,sample,check,edit_work,delete,del_date
from app_1.views import hii

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",signup,name="signup"),
    path("user_signup",user_signup,name="user_signup"),
    path("login",login,name="login"),
    path("user_login",user_login,name="user_login"),
    path("home",sample,name="home"),
    path("select_date",date,name="select_date"),
    path("insert",insert,name="dt"),
    path("save_work",save_work,name="work"),
    path("edit",edit,name="edit"),
    path("check",check,name="check"),
    path("edit_work",edit_work,name="edit_work"),
    path("delete",delete,name="delete"),
    path("del_date",del_date,name="del_date"),
    path("time_table",time_table,name="time_table"),
    path("view",view,name="view"),
    path("password_reset",password_reset,name="password_reset"),
    path("forgot_password",forgot_password,name="forgot_password"),
    path("hello",hii,name="hii"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
