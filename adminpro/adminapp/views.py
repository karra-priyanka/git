from django.shortcuts import render
from .models import studentdata
# Create your views here.
def Home(request):
    
        data=studentdata.objects.all()
        return render(request,'demo.html',{'data':data})