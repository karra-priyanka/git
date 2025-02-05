"""
URL configuration for curdpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from curdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage),
    path('IndexPage/',views.Back,name='IndexPage'),
    path('add_student/',views.AddStudent,name='add_student'),
    path('updata_date/<id>',views.updateData,name='updata_date'),
    path('update_row/<id>',views.updaterow,name='update_row'),
    path('delete_data/<id>',views.deleteData,name='delete_data')

]
