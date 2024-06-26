from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    isActive=True
    if request.method=='POST':
       check=request.POST.get("check")
    print("check")
    if check is  None: isActive=False
    else: isActive=True



    date=datetime.datetime.now()
    
    name="gourav sekhar senapati"
    list_of_programs=[
        'wap  to check even or odd',
        'wap to check prime number',
        'wap to print all prime numbers from 1 to 100',
        'wap to print pascals tringle'
    ]
    student={
        'student_name':"rahul",
        'student_college':"xyz",
        'student_city':'cuttack',
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student,

    }
    print("test function is called my view")
    return render(request,"home.html",data)
def about(request):
    return render(request,"about.html",{})
def services(request):
    return render(request,"services.html",{})