from django.shortcuts import render
from .models import ContactForm
from django.http import HttpResponse

# Create your views here.
def contactform(request):
    if request.method=="GET":
        data=ContactForm.objects.all().order_by('-id')
        return render(request,'facebook.html',{'data':data})
    else:
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        iname=request.POST.get('iname')
        address=request.POST.get('address')
 

    ContactForm(
        first_name=first_name,
        last_name=last_name,
        email=email,
        number=number,
        iname=iname,
        address=address
        ).save( )
    data=ContactForm.objects.all().order_by('-id')
    return render(request,'facebook.html',{'data':data})
 