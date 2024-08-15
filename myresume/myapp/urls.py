from django.urls import path, include

from. import views
app_name= 'myapp'

urlpatterns =[ 
    path('',views.home , name= 'home'),
    
    path('/about',views.about , name= 'about'),
    
    path('/projects',views.projects , name= 'projects'),
    
    path('/contact',views.contact, name= 'contact'),
    
    ]