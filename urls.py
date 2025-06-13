from myform import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.register, name= 'register'),
    path('admin/', admin.site.urls),
]
