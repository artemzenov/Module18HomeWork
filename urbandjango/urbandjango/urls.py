"""
URL configuration for urbandjango project.

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
from task2.views import index
from task2.views import Index
# from task3.views import main_page
# from task3.views import shop
# from task3.views import cart
from task4.views import main_page
from task4.views import shop
from task4.views import cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1', index),
    path('index2', Index.as_view(),),
    path('platform', main_page),
    path('platform/shop', shop),
    path('platform/cart', cart)
]
