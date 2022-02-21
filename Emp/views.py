from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Employee, Role, Department, Register
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


# def index(request):
#     return render(request,'index.html')

def SignUp(request):
    # if request.method == 'POST': 
    #     username = request.POST['username']
    #     fname  = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     myuser = User.objects.create_user(username=username,email=email,password=password)
    #     myuser.first_name = fname
    #     myuser.last_name = lname
    #     myuser.save()
    #     return render(request,'Signup.html',{'msg':'Registration successful'})
    # else:
    #     # return render(request,'SignUp.html',{'errors':'All the fields are mandatory'})
    #     return render(request,'SignUp.html')

    if request.method == 'POST':
        obj = Register(user_name=request.POST['username'],
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['email'],
        password = request.POST['password'])
        obj.save()
        return render(request,'Signup.html',{'msg':'Registration successful'})
    else:
        return render(request,'SignUp.html',{'err':'All the fields are mandatory'})


def LogIn(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
        
    #     user = authenticate(username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         fname = user.first_name
    #         return render(request,"home.html",{'fname':fname})
    #     else:
    #         return render(request,"SignUp.html",{'error':'Bad credentials'})
            
    # return render(request,'SignUp.html')
    s = Register.objects.filter(user_name=request.POST['username'],password=request.POST['password'])
    if s:
        return render(request,'home.html')
    else:
        return render(request,"SignUp.html",{'error':'Bad credentials'})




def SignOut(request):
    logout(request)
    # return render(request,'SignUp.html',{'msgs':'Logged Out Successful'})
    messages.success(request,"Logged out Successfully")
    return redirect("SignUp")

def home(request):
    return render(request,"home.html")


def view_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp
    }
    return render(request,"view_emp.html", context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        department = int(request.POST['department'])
        phone = int(request.POST['phone'])
        hiredate = request.POST['hiredate']
        newemp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,role_id=role,dept_id=department,phone=phone,hiredate=datetime.now())
        newemp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An exception occured! Employee cannot be added.")

def delete_emp(request, emp_id =0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid Id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'delete_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['department']
        role = request.POST['role']
       
        emp = Employee.objects.all()
        
        if name:
            emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
            
        if role:
            emp = emp.filter(role__name__icontains =role)
        if dept:
            emp = emp.filter(dept__name__icontains =dept)
        
        context = {
            'emp':emp
        }
        return render(request,'view_emp.html', context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An exception occured.")       
    # return render(request,'filter_emp.html')