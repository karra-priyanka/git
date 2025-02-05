from django.shortcuts import render,redirect
from .models import FakeData
import faker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
fake=faker.Faker()
def Add(request):
    for _ in range(100):
        FakeData(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            company = fake.random_element(elements=['TCS', 'Infosis', 'Wipro', 'ZOHO', 'Gooogle', 'Amazan']),
            location = fake.random_element(elements=['Hyderabad', 'Banagalor', 'Chennai', 'Delhi', 'Vizag']),
            salary = fake.random_element(elements= [15000, 20000, 30000, 40000, 50000]),
            emp_id = fake.random.randint(10000, 999999),
            address = fake.address()            
            
        ).save()
    return redirect(fakedata)
def fakedata(request):
        if request.method== 'GET':
            data=FakeData.objects.all()
            page = request.GET.get('page', 1)

            paginator = Paginator(data, 50)
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)

            return render(request, 'fake.html', { 'data': users })
            #return render(request,'fake.html',{'data':data})
        else :
            company_data = request.POST.get('company') 
            if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data)
                )  
            else :return render(request, 'fake.html', {'data': data})   
            return render(request, 'fake.html', {'data': data})    
            
def Hyderabad(request): 
    if request.method == 'GET' :   
        data = FakeData.objects.filter(location = 'Hyderabad')
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 50)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'fake.html', { 'data': users })
        #return render(request,'fake.html', {'data': data})
    else :
        company_data = request.POST.get('company')
        if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data) 
                )  
                data = data.filter(location = 'Hyderabad')
        else :return render(request, 'fake.html', {'data': data})   
        return render(request, 'fake.html', {'data': data})    
            
        #data = FakeData.objects.filter(location = 'Hyderabad') & FakeData.objects.filter(company=company_data)
        #return render(request,'fake.html', {'data': data})
def Banagalor(request): 
    if request.method == "GET" :   
        data = FakeData.objects.filter(location = 'Banagalor')
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 50)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'fake.html', { 'data': users })
        #return render(request,'fake.html',{'data': data})
    else :
        company_data = request.POST.get('company')
        if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data)
                )  
                data = data.filter(location = 'Hyderabad')
        else :return render(request, 'fake.html', {'data': data})   
        return render(request, 'fake.html',{'data': data})    
            
        #data = FakeData.objects.filter(location = 'Banagalor') 
        #return render(request,'fake.html', {'data': data})
def Chennai(request):   
    if request.method == 'GET' :
        data = FakeData.objects.filter(location = 'Chennai')
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 50)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'fake.html', { 'data': users })
        #return render(request,'fake.html', {'data': data})
    else :
        company_data = request.POST.get('company')
        if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data)
                )  
                data = data.filter(location = 'Chennai')
        else :return render(request, 'fake.html', {'data': data})   
        return render(request, 'fake.html',{'data': data})    
        #data = FakeData.objects.filter(location = 'Chennai') & FakeData.objects.filter(company=company_data) 
        #return render(request,'fake.html', {'data': data})
    
def Delhi(request): 
    if request.method == 'GET':  
        data = FakeData.objects.filter(location = 'Delhi')
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 50)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'fake.html', { 'data': users })
        #return render(request,'fake.html', {'data': data})
    else :
        company_data = request.POST.get('company')
        if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data)
                )  
                data = data.filter(location = 'Delhi')
        else :return render(request, 'fake.html', {'data': data})   
        return render(request, 'fake.html',{'data': data})    
        #data = FakeData.objects.filter(location = 'Delhi') & FakeData.objects.filter(company=company_data) 
        #return render(request,'fake.html', {'data': data})
def Vizag(request):
    if request.method == 'GET' :    
        data = FakeData.objects.filter(location = 'Vizag')
        page = request.GET.get('page', 1)
        paginator = Paginator(data, 50)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request, 'fake.html', { 'data': users })
        #return render(request,'fake.html', {'data': data})
    else :
        company_data = request.POST.get('company')
        if company_data :
                data = FakeData.objects.filter(
                Q(first_name__icontains= company_data) |
                Q(last_name__icontains = company_data) |
                Q(email__icontains = company_data) |
                Q(company__icontains = company_data) |
                Q(location__icontains= company_data) |
                Q(salary__icontains = company_data)|
                Q(emp_id__icontains = company_data) |
                Q(address__icontains = company_data)
                )  
                data = data.filter(location = 'Vizag')
        else :return render(request, 'fake.html', {'data': data})   
        return render(request, 'fake.html',{'data': data})    
        #data = FakeData.objects.filter(location = 'Vizag') & FakeData.objects.filter(company=company_data)
        #return render(request,'fake.html', {'data': data})