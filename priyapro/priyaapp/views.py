from django.shortcuts import render,redirect
from .models import indexpage
# Create your views here.
def Home(request):
    data=indexpage.objects.all()
    return render(request,'homepage.html',{'data':data})
def AddStudent(request):
    if request.method=='GET':
        data=indexpage.objects.all()
        return render(request,'add_student.html',{'data':data})
    else:
        indexpage(
            f_name=request.POST.get('f_name'),
            l_name=request.POST.get('l_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address')    
        ).save()
        return redirect(Home) 
def Back(request):
    return redirect(Home)
def updateData(request,id):
    row = indexpage.objects.get(id=id)
    return render(request,'update.html', {'row':row})
def updaterow(request,id):
    data=indexpage.objects.get(id=id)
    data.f_name=request.POST.get('fname')
    data.l_name=request.POST.get('lname')
    data.email=request.POST.get('email')
    data.address=request.POST.get('address')
    data.save()
    return redirect(Home)
def Delete(request,id):
    data=indexpage.objects.get(id=id)
    data.delete()
    return redirect(Home)
