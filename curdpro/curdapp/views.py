from django.shortcuts import render,redirect
from .models import indexPage
# Create your views here.
def indexpage(request):
    data=indexPage.objects.all()
    return render(request,'IndexPage.html',{'data':data})
def AddStudent(request):
    if request.method=='GET':
        data=indexPage.objects.all()
        return render(request,'add_student.html',{'data':data})
    else:
        indexPage(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            institute=request.POST.get('institute')
        ).save( )
        data=indexPage.objects.all()
        return redirect(indexpage) 
def Back(request):
    return redirect(indexpage)
def deleteData(request,id):
    data=indexPage.objects.get(id=id)
    data.delete()
    return redirect(indexpage)
def updateData(request,id):
    row = indexPage.objects.get(id=id)
    return render(request,'update.html', {'row':row})

def updaterow(request,id):
    data=indexPage.objects.get(id=id)
    data.first_name=request.POST.get('fname')
    data.last_name=request.POST.get('lname')
    data.email=request.POST.get('email')
    data.address=request.POST.get('address')
    data.institute=request.POST.get('institute')
    data.save()
    return redirect(indexpage)