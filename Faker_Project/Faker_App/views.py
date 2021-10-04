
from django.shortcuts import render,redirect
from Faker_App.models import Employee

from faker import Faker
fake = Faker()

def create_fake_data_view(request):
    for i in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.random_element(elements=('Srinivas','Dinesh','Rajesh',"Amol","Pooja"))
        email = fake.email()
        role = fake.random_element(elements=('SE','TL','MGR',"PM","JR"))
        salary = fake.random_element(elements=(10000,20000,30000,40000,50000))
        city = fake.random_element(elements=('Hyderabad','Chennai','Mumbai',"Pune","Bangaloor"))
        mobile = fake.random_int(min=9000,max=999999)

        Employee.objects.create(
            first_name=first_name,last_name=last_name,
            username=username,email=email,role=role,
            salary=salary,city=city,mobile=mobile
        )
        # emp = Employee(.....)
        # emp.save()
    return redirect('/accessing_fake_data/')

def accessing_fake_data_view(request):
    employee_list = Employee.objects.all()
    count = Employee.objects.all().count()
    managers = Employee.objects.filter(role="MGR").count()
    context = {
        "employee_list" : employee_list,
        'count' : count,
        'managers' : managers
    }
    return render(request,'display_data.html',context)






