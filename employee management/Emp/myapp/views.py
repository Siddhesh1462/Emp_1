from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def view(request,emp_id = 0):
    if emp_id:
        try :
            emp_to_be_removed= Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee deleted successfully!!!!")
        except:
            return HttpResponse("please select valid id!!!!")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view.html',context)

def add(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        phone = int(request.POST['phone'])
        dept =  int(request.POST['dept'])
        role =  int(request.POST['role'])
        salary =  int(request.POST['salary'])
        bonus =  int(request.POST['bonus'])
        hire_date =  int(request.POST['hire_date'])

        new_emp= Employee(f_name=f_name , l_name=l_name, phone=phone, dept_id=dept, role_id=role, salary=salary,bonus=bonus, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("employee added successfully!!!!")
    
    elif request.method == 'GET':
        return render(request,'add.html')
    else:
        return HttpResponse("an Exception is occured!!!!")

def update(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        # l_name = request.POST['l_name']
        dept =  request.POST['dept']
        role =  request.POST['role']

        emps = Employee.objects.all()
        if f_name:
            emps = emps.filter(f_name__icontains = f_name)
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request,'view.html',context)
    
    elif request.method == 'GET':
        return render (request,'update.html')
    else:
        return HttpResponse('invalid!')




    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')