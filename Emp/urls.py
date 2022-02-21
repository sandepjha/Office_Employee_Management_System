from django.urls import path
from . import views


urlpatterns =[
    # path('',views.index, name='index'),
    path('',views.SignUp, name='SignUp'),
    path('LogIn',views.LogIn, name='LogIn'),
    path('SignOut',views.SignOut, name='SignOut'),
    path('home', views.home,name='home'),
    path('view_emp',views.view_emp, name='view_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('delete_emp',views.delete_emp,name='delete_emp'),
    path('delete_emp/<int:emp_id>',views.delete_emp,name='delete_emp'),
    path('filter_emp',views.filter_emp,name='filter_emp'),
]